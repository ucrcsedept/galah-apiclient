def pretty_list(the_list, conjunction = "and", none_string = "nothing"):
    """
    Returns a grammatically correct string representing the given list. For
    example...

    >>> pretty_list(["John", "Bill", "Stacy"])
    "John, Bill, and Stacy"
    >>> pretty_list(["Bill", "Jorgan"], "or")
    "Bill or Jorgan"
    >>> pretty_list([], none_string = "nobody")
    "nobody"

    """

    the_list = list(the_list)

    if len(the_list) == 0:
        return none_string
    elif len(the_list) == 1:
        return str(the_list[0])
    elif len(the_list) == 2:
        return str(the_list[0]) + " " + conjunction + " " + str(the_list[1])
    else:
        # Add every item except the last two together seperated by commas
        result = ", ".join([str(s) for s in the_list[:-2]]) + ", "

        # Add the last two items, joined together by a command and the given
        # conjunction
        result += "%s, %s %s" % \
            (str(the_list[-2]), conjunction, str(the_list[-1]))

        return result

def plural_if(zstring, zcondition):
    """
    Returns zstring pluralized (adds an 's' to the end) if zcondition is True or
    if zcondition is not equal to 1.

    Example usage could be ``plural_if("cow", len(cow_list))``.

    """

    # If they gave us a boolean value, just use that, otherwise, assume the
    # value is some integral type.
    if type(zcondition) is bool:
        plural = zcondition
    else:
        plural = zcondition != 1

    return zstring + ("s" if plural else "")
