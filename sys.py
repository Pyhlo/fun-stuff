import sys
import os
import platform
import time
import wmi


computer = wmi.WMI()
def getInfo():

    os.system('clear')

    print('Getting information on your system...')

    ## OS
    mySys = platform.platform()
    sysNode = platform.node()
    processor = platform.processor()
    caption = computer.Win32_OperatingSystem()[0].caption
    windowsDirectory = computer.Win32_OperatingSystem()[0].WindowsDirectory
    registeredAs = computer.Win32_OperatingSystem()[0].RegisteredUser
    systemRam = float(computer.Win32_OperatingSystem()[0].TotalVisibleMemorySize) / 1048576
    systemRam = round(float(systemRam), 2)

    os.system('clear')
    print('Getting information on your processor...')
    ## PROCESSOR
    myCpu = computer.Win32_Processor()[0].Name
    currentVoltage = computer.Win32_Processor()[0].CurrentVoltage
    numOfCores = computer.Win32_Processor()[0].NumberOfCores
    numOfEnabledCores = computer.Win32_Processor()[0].NumberOfEnabledCore
    socketDesignation = computer.Win32_Processor()[0].SocketDesignation

    os.system('clear')
    print('Getting information on your GPU...')
    ## GPU
    myGpu = computer.Win32_VideoController()[0].Name
    memoryType = computer.Win32_VideoController()[0].VideoMemoryType
    maxRefresh = computer.Win32_VideoController()[0].MaxRefreshRate
    minRefresh = computer.Win32_VideoController()[0].MinRefreshRate

    os.system('clear')
    print('''
 _  _  _ _____ __   _ ______   _____  _  _  _ _______      _____ __   _ _______  _____
 |  |  |   |   | \  | |     \ |     | |  |  | |______        |   | \  | |______ |     |
 |__|__| __|__ |  \_| |_____/ |_____| |__|__| ______|      __|__ |  \_| |       |_____|
                                    v1.0 By Pyhlo''')
    print('[**] OS System information [**]')
    print('System: ' + str(mySys))
    print('Node: '+ str(sysNode))
    print('Caption: ' + str(caption))
    print('Directory of Windows: ' + str(windowsDirectory))
    print('Registered Email: ' + str(registeredAs))
    print('System RAM: ' + str(systemRam))
    print(' ')
    print('[**] Processor information [**]')
    print('Processor: ' + str(myCpu))
    print('Current voltage: ' + str(currentVoltage))
    print('Number of cores: ' + str(numOfCores))
    print('Number of enabled cores: ' + str(numOfEnabledCores))
    print('Socket designation: ' + str(socketDesignation))
    print(' ')
    print('[**] GPU Information [**]')
    print('GPU: ' + str(myGpu))
    print('Memory type: ' + str(memoryType))
    print('Max refresh rate: ' + str(maxRefresh))
    print('Min refresh rate: ' + str(minRefresh))
    print(' ')
    time.sleep(10000)
getInfo()
