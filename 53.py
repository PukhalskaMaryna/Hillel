import string
hashtag = input("введіть дані: ").title().replace(" ","")
for i in string.punctuation:
    hashtag = hashtag.replace(i,"")
print("#" + hashtag[:139]) # обрізає 140 перших символів, враховуючи "#", вказати 140 замість 139, якщо не враховувати "#"
