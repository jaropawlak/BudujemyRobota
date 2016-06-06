using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Net.Http;
using Windows.ApplicationModel.Background;
using Windows.Networking.Sockets;
using Windows.ApplicationModel.AppService;
using System.Threading.Tasks;
using Windows.Storage.Streams;
using System.Runtime.InteropServices.WindowsRuntime;
using System.IO;
using Windows.Foundation.Collections;

// The Background Application template is documented at http://go.microsoft.com/fwlink/?LinkID=533884&clcid=0x409

namespace RobotHttpRestServer
{
    public sealed class StartupTask : IBackgroundTask
    {
        BackgroundTaskDeferral serviceDeferral;
        HttpServer httpServer;

        public void Run(IBackgroundTaskInstance taskInstance)
        {
            // Get the deferral object from the task instance
            serviceDeferral = taskInstance.GetDeferral();

            httpServer = new HttpServer(8000);
            httpServer.StartServer();
        }

    }

    public sealed class HttpServer : IDisposable
    {
        private const string prefix = "<html><head><title>ROBOT CONTROL</title></head><body>";
        private const string postfix = "</body></html>";
        private const uint BufferSize = 8192;
        private int port = 8000;
        private StreamSocketListener listener;
        private AppServiceConnection appServiceConnection;

        public HttpServer(int serverPort)
        {
            listener = new StreamSocketListener();
            listener.Control.KeepAlive = true;
            listener.Control.NoDelay = true;

            port = serverPort;
            listener.ConnectionReceived += async (s, e) => { await ProcessRequestAsync(e.Socket); };
        }

        public void StartServer()
        {
            Task.Run(async () =>
            {
                await listener.BindServiceNameAsync(port.ToString());

                // Initialize the AppServiceConnection
                appServiceConnection = new AppServiceConnection();
                appServiceConnection.PackageFamilyName = "RobotService_HttpModule";
                appServiceConnection.AppServiceName = "RobotService";

                // Send a initialize request 
                var res = await appServiceConnection.OpenAsync();
                if (res != AppServiceConnectionStatus.Success)
                {
                    throw new Exception("Failed to connect to the AppService");
                }
            });
        }


        public void Dispose()
        {
            listener.Dispose();
        }

        private async Task ProcessRequestAsync(StreamSocket socket)
        {
            // this works for text only
            StringBuilder request = new StringBuilder();
            byte[] data = new byte[BufferSize];
            IBuffer buffer = data.AsBuffer();
            uint dataRead = BufferSize;
            using (IInputStream input = socket.InputStream)
            {
                while (dataRead == BufferSize)
                {
                    await input.ReadAsync(buffer, BufferSize, InputStreamOptions.Partial);
                    request.Append(Encoding.UTF8.GetString(data, 0, data.Length));
                    dataRead = buffer.Length;
                }
            }

            string requestAsString = request.ToString();
            string[] splitRequestAsString = requestAsString.Split('\n');
            if (splitRequestAsString.Length != 0)
            {
                string requestMethod = splitRequestAsString[0];
                string[] requestParts = requestMethod.Split(' ');
                if (requestParts.Length > 1)
                {
                    if (requestParts[0] == "GET")
                        WriteResponse(requestParts[1], socket);
                    else
                        throw new InvalidDataException("HTTP method not supported: "
                            + requestParts[0]);
                }
            }
        }

        private void WriteResponse(string request, StreamSocket socket)
        {
            // See if the request is for blinky.html, if yes get the new state
            string command = string.Empty;
            bool stateChanged = false;
            if (request.Contains(".html?command="))
            {
                 command = request.Substring(request.IndexOf(".html?command=") + 14).ToUpper();
              
            }

            if (stateChanged)
            {
                var updateMessage = new ValueSet();
                updateMessage.Add("Command", command);
#pragma warning disable CS4014
                appServiceConnection.SendMessageAsync(updateMessage);
#pragma warning restore CS4014
            }

            string html = prefix + command + postfix;
            byte[] bodyArray = Encoding.UTF8.GetBytes(html);
            // Show the html 
            using (var outputStream = socket.OutputStream)
            {
                using (Stream resp = outputStream.AsStreamForWrite())
                {
                    using (MemoryStream stream = new MemoryStream(bodyArray))
                    {
                        string header = String.Format("HTTP/1.1 200 OK\r\n" +
                                            "Content-Length: {0}\r\n" +
                                            "Connection: close\r\n\r\n",
                                            stream.Length);
                        byte[] headerArray = Encoding.UTF8.GetBytes(header);
                        resp.Write(headerArray, 0, headerArray.Length);
                        stream.CopyTo(resp);
                        resp.Flush();
                    }
                }
            }
        }
    }
}
