#!/bin/bash

today=$(date)									#we made our command become variable just keep in mind that for the syntax VARIABLE=$(command)	
target=$1									#in bash $1 refers for argument 1 and $2 is so on
directory=$target								#bash for variable is variable=value

echo "making directory of $target"						#for the echo command you should give him scape
mkdir -p $directory

nmap_scan()									#for making function the syntax is function_name()
{								   			#use curly bracket 	   {
	nmap -sT $target -F -T4 > $directory/nmap.txt					#			   }
	cat $directory/nmap.txt
	echo "---------------nmap-----------------"
	echo "this scan was created $today"
}
gobuster_scan()
{
	gobuster dir --url $target --wordlist /usr/share/wordlists/dirb/small.txt > $directory/gobuster.txt
	cat $directory/gobuster.txt
	echo "---------------------gobuster---------------"
	echo "the result of gobuster scan in $directory/gobuster.txt"
}
eyewitness_scan()
{
	eyewitness --web -f listdirectory.txt --timeout 4 --no-prompt -d $directory/eyewitness
        echo "-------------------eyewitness---------------"
        echo "the result of gobuster scan in $directory/eyewitness"
}

getopts "m": OPTION		#getopts adalah built-in command di shell yang digunakan untuk mem-parsing opsi dari argumen yang diberikan saat menjalankan skrip.
				#Dalam contoh ini, m: menunjukkan bahwa ada opsi -m yang memerlukan argumen. Tanda titik dua (:) setelah m berarti bahwa pengguna harus memberikan nilai setelah opsi ini, misalnya -m nilai.
				#OPTION adalah variabel yang akan menyimpan karakter opsi yang sedang diproses. Jika pengguna memberikan -m, maka OPTION akan berisi m.

MODE=$OPTARG			#Setelah getopts memproses opsi, nilai argumen yang diberikan untuk opsi -m akan disimpan dalam variabel MODE.
				#OPTARG adalah variabel khusus yang menyimpan nilai dari argumen yang terkait dengan opsi yang sedang diproses. Jadi, jika pengguna menjalankan skrip dengan -m mode1, maka MODE akan berisi mode1

for i in "$(@:OPTIND:$#)"	#baris ini memulai sebuah loop yang akan mengulangi setiap argumen yang tersisa setelah opsi diproses.
				# kurung dua dollar @ mewakili semua argumen yang diberikan ke skrip.
				#OPTIND adalah variabel yang menunjukkan indeks argumen berikutnya yang akan diproses oleh getopts.
				#Sintaks setelah if mengambil semua argumen mulai dari indeks OPTIND hingga akhir daftar argumen. Ini berarti bahwa loop ini hanya akan memproses argumen yang tersisa setelah opsi.

do
	case $2 in								 #the case syntax is ( case $variable in )

		nmap-only)							 #	case1)
			nmap_scan						 #		do something
			;;
		gobuster-only)
			gobuster_scan
			;;
		eyewitness-only)
			eyewitness_scan
			;;
		*)								#* means execute command if you don't give argument
			nmap_scan
			gobuster_scan
			eyewitness_scan
			;;
	esac									#for end of case use ( esac )

	echo "generating report for $target"
	echo "this scan was created $today" > $directory/report

	if [ -f $directory/nmap.txt ]; then              #opsi -f digunakan untuk mengecek apakah file tersebut ada sebelum diproses
	#dalam shell ada banyak operator untuk memeriksa berbagai kondisi contoh: #-f untuk mengecek file ada #-d untuk mengecek direktori itu ada
	#-e untuk memerikasa file atau direktori itu ada   -s untuk memeriksa apakah file itu berisi serta tidak kosong
	#-w untuk memeriksa file itu bisa di write/tulis   -x untuk memeriksa apakah file itu bisa di execute/eksekusi
	#-r untuk memeriksa file itu bisa di read/dibaca   -z Memeriksa apakah panjang string adalah nol (0). Dengan kata lain, operator ini digunakan untuk memeriksa apakah string kosong.
	#-n untuk Memeriksa apakah panjang string lebih dari nol (0). Dengan kata lain, operator ini digunakan untuk memeriksa apakah string tidak kosong.

	#dibawah ini untuk  membadingkan angka
	# -lt less than (kurang dari)	# -le less than or equal to (kurang dari atau sama dengan)
	# -gt greater than (lebih dari  # -ge greater than or equal to (lebih dari atau sama dengan)
	# -eq equal to (sama dengan)	# -ne not equal to (tidak sama dengan)


		echo "the report of nmap scan in $directory/report"
		grep -E "^\S+\s+\S+\s+\S+$" $directory/nmap.txt >> $directory/report	#we use -E so grep know we use regex and \s mean match any whitespaces \S match any non whitespaces in this case [PORT STATE SERVICE]
		# * match preceeding zero or more times					# ^ match start of the string in line. where $ match end string in line
		# + match preceeding character one or more times			# \ escape special character. \w match any character. \d match any digit
		# {3} match the preeceeding character 3 time
		# {1, 3} match the preeceeding character 1 or 3 time
		# {1, } match the preeceeding character 1 or 3 time			# . match with any single character 
		# [abc] match one of the character within bracket
		# [a-z] match one of the character within the range a to z bracket
		# (a|b|c) match a or b or c
	fi

	if [ -f $directory/gobuster.txt ]; then
		echo "the report of gobuster scan in $directory/report"
		cat $directory/gobuster.txt >> $directory/report
	fi
done
