#!/bin/bash
rm -rf lresult.txt gresult.txt lresult1.txt test.txt lresult2.txt gresult2.txt Gradle_Distributions.html Index_of_distributions.html
python localserver.py 2>&1 | tee lresult.txt
python gradleserver.py 2>&1 | tee gresult.txt
sed -i '/\<gradle\>/I! d' lresult.txt
sed -i '1,19d' gresult.txt
tac lresult.txt > lresult1.txt
sed -i s/[[:space:]]//g lresult1.txt
awk '{print length,$0}' lresult1.txt | sort -n | sed 's/.* //' > lresult2.txt
awk '{print length,$0}' gresult.txt | sort -n | sed 's/.* //' > gresult2.txt
diff -n lresult2.txt gresult2.txt > test.txt
sed -i '/\<gradle\>/I! d' test.txt
echo '!-----Download Start-----!'
for line in $(cat test.txt)
do
 echo 'download new gradle files'
 echo $line
 wget -P /usr/local/apache2/htdocs/distributions "https://services.gradle.org/distributions/$line"
done
echo '!-----FINISH-----!'
