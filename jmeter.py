"""
#!/bin/sh

export JMeter_Home=

if [ ! -f $JMeter_Home/bin/ApacheJMeter.jar ];then
#如果ApacheJMeter.jar不存在，则运行gradle编译创建
echo “ApacheJMeter.jar不存在”
cd $JMeter_Home
#sh gradlew clean runGui
sh gradlew runGui
else
#如果ApacheJMeter.jar存在，则直接运行Jmeter
sh $JMeter_Home/bin/jmeter.sh
fi


"""