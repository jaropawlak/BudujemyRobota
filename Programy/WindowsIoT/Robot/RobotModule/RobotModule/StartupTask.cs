using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Net.Http;
using Windows.ApplicationModel.Background;
using Windows.ApplicationModel.AppService;

// The Background Application template is documented at http://go.microsoft.com/fwlink/?LinkID=533884&clcid=0x409

namespace RobotModule
{
    public sealed class StartupTask : IBackgroundTask
    {
        private BackgroundTaskDeferral deferral;
        private AppServiceConnection appServiceConnection;
        HardwareController hardware = new HardwareController();
        public void Run(IBackgroundTaskInstance taskInstance)
        {
            deferral = taskInstance.GetDeferral();
            var appService = taskInstance.TriggerDetails as AppServiceTriggerDetails;
            if (appService != null &&
                appService.Name == "RobotService")
            {
                appServiceConnection = appService.AppServiceConnection;
                appServiceConnection.RequestReceived += OnRequestReceived;
            }
        }
        private void OnRequestReceived(AppServiceConnection sender, AppServiceRequestReceivedEventArgs args)
        {
            var messageDefferal = args.GetDeferral();
            var message = args.Request.Message;
            string command = message["Command"] as string;
            // Command: F B L R FL BL FR BR STOP
            messageDefferal.Complete();

            switch (command)
            {
                case "F": //forward
                    hardware.GoForward(100); break;
                case "B": //back
                    hardware.GoBack(100); break;
                case "L": //letf
                    hardware.StartTurningLeft(100,100); break;
                case "R": //right
                    hardware.StartTurningRight(100,100); break;
                case "FL": //forward left
                    hardware.LeftEngineForward(100); break;
                case "BL": //back left
                    hardware.LeftEngineBackward(100); break;
                case "FR": //forward right
                    hardware.RightEngineForward(100); break;
                case "BR": //Back Right
                    hardware.RightEngineBackward(100); break;
                case "STOP": //stop
                    hardware.Stop(); break;

            }
        }
    }
}
