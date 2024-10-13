def longestCommonPrefix(strs):
    # Return an empty string if the input list is empty
    if not strs:
        return ""

    # Initialize the prefix with the first string in the list
    prefix = strs[0]

    # Compare the prefix with each string in the list, starting from the second string
    for string in strs[1:]:
        # While the current string does not start with the prefix,
        # shorten the prefix by removing the last character
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            # If the prefix becomes empty, return an empty string
            if not prefix:
                return ""

    return prefix


print(longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"

print(longestCommonPrefix(["dog", "racecar", "car"]))    # Output: ""