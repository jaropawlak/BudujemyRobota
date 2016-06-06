using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Windows.Devices.Gpio;
namespace RobotModule
{
    public sealed class HardwareController
    {
        private GpioController gpioController;

        private GpioPin leftEngine1;
        private GpioPin leftEngine2;

        private GpioPin rightEngine1;
        private GpioPin rightEngine2;


        public HardwareController()
        {
            Init();
        }
        private void Init()
        {
            gpioController =GpioController.GetDefault();
            if (gpioController != null)
            {
                leftEngine1 = gpioController.OpenPin(leftEngine1Pin);
                leftEngine1.SetDriveMode(GpioPinDriveMode.Output);
                leftEngine1.Write(GpioPinValue.Low);

                leftEngine2 = gpioController.OpenPin(leftEngine2Pin);
                leftEngine2.SetDriveMode(GpioPinDriveMode.Output);
                leftEngine2.Write(GpioPinValue.Low);

                rightEngine1 = gpioController.OpenPin(rightEngine1Pin);
                rightEngine1.SetDriveMode(GpioPinDriveMode.Output);
                rightEngine1.Write(GpioPinValue.Low);

                rightEngine2 = gpioController.OpenPin(rightEngine2Pin);
                rightEngine2.SetDriveMode(GpioPinDriveMode.Output);
                rightEngine2.Write(GpioPinValue.Low);
            }
        }


        public void Stop()
        {
            leftEngine1.Write(GpioPinValue.Low);
            leftEngine2.Write(GpioPinValue.Low);
            rightEngine1.Write(GpioPinValue.Low);
            rightEngine2.Write(GpioPinValue.Low);
        }
       
        public void LeftEngineForward(int power)
        {
            leftEngine1.Write(GpioPinValue.High);
            leftEngine2.Write(GpioPinValue.Low);
        }
        public void LeftEngineBackward(int power)
        {
            leftEngine1.Write(GpioPinValue.Low);
            leftEngine2.Write(GpioPinValue.High);
        }
        public void RightEngineForward(int power)
        {
            leftEngine1.Write(GpioPinValue.High);
            leftEngine2.Write(GpioPinValue.Low);
        }
        public void RightEngineBackward(int power)
        {
            leftEngine1.Write(GpioPinValue.Low);
            leftEngine2.Write(GpioPinValue.High);
        }

        public void GoForward(int power)
        {
            LeftEngineForward(power);
            RightEngineForward(power);
        }

        public void GoBack(int power)
        {
            LeftEngineBackward(power);
            RightEngineBackward(power);
        }

        public void StartTurningLeft(int leftPower, int rightPower )
        {
            LeftEngineBackward(leftPower);
            RightEngineForward(rightPower);
        }
        public void StartTurningRight(int leftPower, int rightPower)
        {
            LeftEngineForward(leftPower);
            RightEngineBackward(rightPower);
        }

        private const int leftEngine1Pin = 17; // header pin 11
        private const int leftEngine2Pin = 27; // header pin 13
        private const int rightEngine1Pin = 22; // header pin 15
        private const int rightEngine2Pin = 23; // header pin 16

    }
}
