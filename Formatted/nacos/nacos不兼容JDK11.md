&emsp;  
&emsp;  
```
/nacos/jdk-11.0.12/bin/java   -server -Xms2g -Xmx2g -Xmn1g -XX:MetaspaceSize=128m -XX:MaxMetaspaceSize=320m -XX:-OmitStackTraceInFastThrow -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/nacos/nacos-server-2.0.3-node1/logs/java_heapdump.hprof -XX:-UseLargePages -Dnacos.member.list= -Xlog:gc*:file=/nacos/nacos-server-2.0.3-node1/logs/nacos_gc.log:time,tags:filecount=10,filesize=102400 -Dloader.path=/nacos/nacos-server-2.0.3-node1/plugins/health,/nacos/nacos-server-2.0.3-node1/plugins/cmdb -Dnacos.home=/nacos/nacos-server-2.0.3-node1 -jar /nacos/nacos-server-2.0.3-node1/target/nacos-server.jar  --spring.config.additional-location=file:/nacos/nacos-server-2.0.3-node1/conf/ --logging.config=/nacos/nacos-server-2.0.3-node1/conf/nacos-logback.xml --server.max-http-header-size=524288
Error: Could not find or load main class 
Caused by: java.lang.ClassNotFoundException: 
```
&emsp;  
```sh
在Nacos-Server的 bin / startup.sh
由JAVA_OPT_EXT_FIX 配置引起启动报错

在startup.sh文件中替换下方配置

x JAVA_OPT_EXT_FIX="-Djava.ext.dirs=${JAVA_HOME}/jre/lib/ext:${JAVA_HOME}/lib/ext"
√ JAVA_OPT="${JAVA_OPT} -Djava.ext.dirs=${JAVA_HOME}/jre/lib/ext:${JAVA_HOME}/lib/ext"

x echo "$JAVA $JAVA_OPT_EXT_FIX ${JAVA_OPT}"
√ echo "$JAVA ${JAVA_OPT}"

x echo "$JAVA $JAVA_OPT_EXT_FIX ${JAVA_OPT}" > ${BASE_DIR}/logs/start.out 2>&1 &
x nohup "$JAVA" "$JAVA_OPT_EXT_FIX" ${JAVA_OPT} nacos.nacos >> ${BASE_DIR}/logs/start.out 2>&1 &
√ echo "$JAVA ${JAVA_OPT}" > ${BASE_DIR}/logs/start.out 2>&1 &
√ nohup $JAVA ${JAVA_OPT} nacos.nacos >> ${BASE_DIR}/logs/start.out 2>&1 &
```
&emsp;  
&emsp;  
