# Learnings from exercise "add"

* In Python, I can have any number of arguments for a function by by having an asterisk unpacking operator! For example:

        from random import randint

        def roll(*dice):
            return sum(randint(1, die) for die in dice)

    can be called like this:

        >>> roll(20)
        18
        >>> roll(6, 6)
        9
        >>> roll(6, 6, 6)
        8

* Comprehensions can be used when looping through lists to add results to a new list
* Zip function is useful to loop through many collections at the same time (stops at length of the shortest list)
* Sum function is used when you have an unknown amount of variables to add
