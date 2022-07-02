from myapp.models import Tweet
import csv
import io

def run():
    with open('myapp/train.csv' , 'r' , encoding='unicode_escape') as file:
        #reader = csv.reader((line.replace('\0','') for line in file), delimiter=",")
        Tweet.objects.all().delete()

        reader = csv.reader(file , delimiter=',')
        next(reader)  # Advance past the header
        Tweet.objects.all().delete()

        for row in reader:
            print(row[0] , row[1] , row[2] , row[3])

            tweet = Tweet(
                        id=row[0],
                        text=row[1],
                        selectedText=row[2],
                        sentiments=row[3])
            tweet.save()