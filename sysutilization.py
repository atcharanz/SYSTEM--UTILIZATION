import subprocess,re

#Ram Usage func
def ramusagecalc():
    #capture meminfo
    meminfo=subprocess.run(['cat','/proc/meminfo'],capture_output=True,text=True)

    #extract required data field from meminfo using regex module('re')
    meminfogrep=subprocess.run(['grep','MemTotal\|MemFree'],capture_output=True,text=True,input=meminfo.stdout)
    meminfogrepsplit=re.split(':|kB', meminfogrep.stdout)

    #values of TotalRAM Memory,FreeRAM Memory,UsedRAM Memory in kB
    memtotal=float(meminfogrepsplit[1])
    memfree=float(meminfogrepsplit[3])
    memused=memtotal-memfree
    #Ram usage calculation in %
    ramusageper=((memused/memtotal))*100

    print('---MEMORY USAGE---')
    print('TotalMemory :'+str(memtotal)+'kB')
    print('FreeMemory :'+str(memfree)+'kB')
    print('UsedMemory :'+str(memused)+'kB')

    #Check RamUsage condition
    if ramusageper < 90:
        return "Memory usage :"+ str(int(ramusageper))+"%. 'Within Limit'"
    elif ramusageper >= 90:
        return "Memory usage :" + str(int(ramusageper)) + "%. 'Outside Limit'"

#CPU usage func
def cpuusagecalc():

    #Capture CPUinfo
    cpuusage= subprocess.getoutput(('top -b -n1 d1'))

    #Extract required data field from CPUinfo
    cpugrep= subprocess.run(['grep', '%Cpu'], capture_output=True,text=True,input=cpuusage)
    cpugrepsplit = re.split(':|us|,|sy,',cpugrep.stdout)

    #Values of uscpu,sycpu,total in %
    uscpu,sycpu=float(cpugrepsplit[1]),float(cpugrepsplit[3])
    totalcpuuse = uscpu + sycpu

    print("---CPU USAGE---")
    cpuusageinfo='TotalCpuUse :'+str(totalcpuuse)+'% ; UsCpuUse :'+str(uscpu)+'% ;SyCpuUse :'+str(sycpu)+'%'
    return cpuusageinfo

#Disc Usage func
def discusage():

    #Capture discusage info
    cmd = "df -kh | awk '{print $1,$2,$3,$5}'|head -n 7"
    discusage = subprocess.getoutput((cmd))

    print("---DISC USAGE---")
    return discusage




if __name__ == '__main__':
    print(ramusagecalc())
    print('\n')
    print(cpuusagecalc())
    print('\n')
    print(discusage())
    print('\n')