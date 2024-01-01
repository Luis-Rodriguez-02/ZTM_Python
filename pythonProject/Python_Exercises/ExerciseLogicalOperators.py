# Wizard game
is_magician = True
is_expert = True

# Check if magician and expert -> print "You are a master magician"
# Check if magician and not expert -> print getting there
# Check if not magician -> print you need magic powers

if is_expert and is_magician:
    print("You are a master magician")
elif is_magician and not is_expert:
    print("You are getting there")
elif not is_magician:
    print("You need powers")
