x = "There are %d types of people." % 10
binary =  "binary"
do_not = "don't"
y = "Those who knows %s and who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: %S." % y

hilarious = false
joke_evaluation =  "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "Thise is the left side of..."
e = "a string with a right side."

print w + e
