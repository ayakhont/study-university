#!/bin/bash
javaProcess=$(ps -aux | grep java)
if [[ $javaProcess != "" ]]
then
 echo $javaProcess
fi