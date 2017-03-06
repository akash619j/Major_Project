filename="Files.txt"

while read -r line
do
    name="$line"
    #echo "Name read from file - $name"
    #$name >> response.txt
    
    curl -u "acc_69dae28e316a7e0:2ad1b0726c41aa100457fb264868f880" http://api.imagga.com/v1/tagging?url=http://self-balanced-opera.000webhostapp.com/$name  >> response.txt
  #  echo -e "\n" >> response
done < "$filename"
