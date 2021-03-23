Copied from this link:
> https://jeremyaguilon.me/blog/a_collection_of_whiteboard_interview_templates

# A Collection of Whiteboard Interview Templates
Freeze up when transitioning from idea to implementation in code interviews? Use this guide to quickly get the skeleton down.

Like I said in a Visualizing Four Key Interview Algorithms, most technical interviews really belong in a small bucket of algorithms. 
Lately, I've taken the time to coach a few engineers. 
Despite their knowledge of these algorithms, they often find that implementing on a white board is (a) intimidating and (b) difficult to prepare for. 
Only when they finally pick up a recipe on how to generally implement these algorithms do they shine.

And so, in my effort to "open-source" interviewing techniques, I'm here to share my mental recipes and code templates for a few common categories: `tree recursion`, `dynamic programming`, and `sliding windows`. 

Hopefully these are even more accessible and easy to reflect on than the slideshow. 
While I discourage memorizing most things, knowing these recipes will smoothen out your interviewing because you won't need to worry about the skeleton structure anymore. You can just think about the hard bits!

Although I contextualize the algorithms with an example prompt, I encourage you to think about how you can apply these templates onto other interview questions.

##  Basic Tree Recursion
Consider the following interview question: Given the root of a binary tree that stores ints, convert the tree in-place such that each node stores the sum of all the elements in its left and right subtree. (GeeksforGeeks link)

Here's my recipe:

1. Create a helper function for your recursion. Why not use the main function? In some cases, you may want to add extra parameters in the recursive stack. Always making a helper will save you this headache.
2. The biggest tip I tell people I coach is to solve for the easiest possible cases. Quite often, this is simply a null node! You can always add extra base cases if needed.
3. "Imagine" you have a magic function that you can pass the left and right subtree to. It will (as in, it better!) return the exact values you need to solve for the current node. Most magical of all, this is the exact function you're writing right now. Extra hint: In this case, it should return the sum of all elements of the subtree you pass to it.
4. Do the relevant operation for the current node.
5. Return something useful for the parent node.

```python
from test_runner import run_test

# step 1
def inplace_sum_helper(root):
    # Step 2. In an interview, I always comment this to be explicit:
    # Base cases:
    if root is None:
        return 0
    # Step 3. Once again, I always comment this:
    # Recursive calls:
    left_solution = inplace_sum_helper(root.left)
    right_solution = inplace_sum_helper(root.right)

    # Step 4. Do something with these values!
    tmp = root.val # we need this later :)
    root.val = left_solution + right_solution
    # Step 5
    return tmp + left_solution + right_solution

def inplace_sum(root):
    return inplace_sum_helper(root)
    
run_test(inplace_sum)
```
Super short and simple. In fact, most tree recursion is simply a DFS with a few extra lines catered towards your problem.

## Dynamic Programming
Consider the following interview question: *Jack is hopping backwards and forwards in an array of size n. He starts in cell 0 and can hop f cells forwards or b cells backwards. He is allowed to jump up to max_jumps times. How many ways can he reach the last cell and finish the game?*

First, why do we even need DP? By definition of a tree, if you do a recursive traversal, you'll never recursively call on a node you have visited before. However, some recursive solutions do allow this to happen. If you could save the solution the first time you hit a "node," you would save a lot of computational time.

The people I coach are often intimidated by this prompt, but I'm here to show you that if you've got the hang of recursion, you can actually write a DP solution using almost the exact same template as above! People often demo DP using a multi-dimensional array, but for many it's simpler to use a recursive technique called memoization, where you cache spots Jack has been before.

Here's my template. Hopefully this sounds familiar to above:

1. Create a helper function for your recursion. It should take all the arguments in the main method plus a dictionary/map. This is memoization.
2. Once again, solve for the easiest cases. What if jack is at the end? What if he is out of moves? What if he fell off the array?
    * **The only difference in DP**: What if Jack was already here? What if at some point, you solved for Jack being in this cell i with n moves left? Assuming that we have our memoized cache, we can just return the solution very quickly.
3. Call the magic function on two branches: Jack jumping backwards and Jack jumping forwards. Also, decrement the number of moves he has left.
4. Solve based on the recursive return values (and store in the cache!!!) and return.

```python
from test_runner import run_test

# step 1
def num_ways_helper(arr, current_index, jumps_left, f, b, cache):
    n = len(arr)

    # Step 2. In an interview, I always comment this to be explicit:
    # Base cases:
    if current_index == n - 1: # we're at the end!
        return 1
    if current_index < 0 or current_index >= n: # Jack fell off the array :(
        return 0
    if jumps_left == 0: # Jack is out of moves :(
        return 0

    # Step 2b. Really the only addition to our recursive recipe
    key = (current_index, jumps_left)
    if key in cache:
        output = cache[key]
        print("Pulling from cache: key = {}, value = {}".format(str(key), jumps_left))
        return cache[key]

    # Step 3. Once again, I always comment this:
    # Recursive calls:
    back_solution = num_ways_helper(arr, current_index - b, jumps_left - 1, f, b, cache)
    forward_solution = num_ways_helper(arr, current_index + f, jumps_left - 1, f, b, cache)

    # Step 4. Remember to cache things for the future
    solution = back_solution + forward_solution
    cache[key] = solution
    return solution

def num_ways(arr, f, b, max_jumps):
    return num_ways_helper(arr, 0, max_jumps, f, b, {})
    
run_test(num_ways)
```

Why do I prefer teaching DP recursively? I find that this framework is way more consistent since it is simply a recursive solution made more efficient by a hash map and a couple lines to read/write into it.

## Sliding Window

Consider the following interview question: *Given a string and a set of characters, return the length of the **smallest** substring that contains all of the characters in the set.* ([GeeksforGeeks link](https://www.geeksforgeeks.org/find-the-smallest-window-in-a-string-containing-all-characters-of-another-string/))

To solve this, you once again need to recognize this as a sliding window problem! The signs are complex to write in words, so view my [visualizations](https://jeremyaguilon.me/blog/visualizing_four_key_interview_algorithms) to learn how.

Now that you recognize this problem, we need to know how to solve it. Here's the high-level recipe:

1. Create two pointers, a left (slow) and a right (fast)
2. Create a "best score found so far." If you're minimizing, make this a big value. If you're maximizing, make it a small value.
3. Create your supporting data structures to track when you've found a valid substring.
4. Create a while right < len(input_string). Note that you may need extra conditionals to handle edge cases for when right is at the end, but you stil have a candidate substring to process. See the code below for this.
    1. If you do not have a candidate substring: increment right and update your data structure.
    2. If you do have a candidate substring: increment left to chop of unecessary letters while updating your data structure.
    3. Update your best score if you now have a smaller string than those found previously.
This is by far the trickiest one to remember. But if you read over this guide and solve a few problems yourself, you'll find that it becomes quite easy to re-implement. Once again in Python:
```python
from test_runner import run_test

def sliding_window(string, char_set):
    # Step 1 and 2
    left, right, best_score = 0, 0, float('inf')

    # Step 3a:  Generally, for sliding window, you often need a set or hashmap to track
    #           the characters/values you have in your substring/subarray
    # Step 3b: This is an auxiliary value that lets us cleanly look up the characters
    #          in char_set that we have found
    letter_map = {} # maps from character to number of occurences in the substring
    characters_encountered = 0 # when this is equal to len(char_set), we have a
                               # candidate substring

    # Step 4: Note the edge case in the conditional. The right pointer may be in the
    #         end, but if the left/right pointers still have all the we want, then
    #         we should increment left to find a new candidate substring.
    while right < len(string) or characters_encountered == len(char_set):
        if characters_encountered != len(char_set):
            # Step 5: Increment the right hand side
            curr_right = string[right]
            if curr_right in char_set:
                letter_map[curr_right] =  letter_map.get(curr_right, 0) + 1
                if letter_map[curr_right] == 1:
                    characters_encountered += 1
            right += 1
        else:
            # Step 6: If you have a new candidate substring (in this case we found all
            #    our letters, begin incrementing left until it is *invalid*.
            curr_left = string[left]
            if curr_left in char_set:
                letter_map[curr_left] -= 1
                if letter_map[curr_left] == 0:
                    characters_encountered -= 1
            left += 1

            # Step 7: Update the best score if we have a new smallest substring.
            #         This new candidate substring is bounded by right - left + 1. Avoid
            #         off-by-one's by drawing an example out.
            best_score = min(best_score, right - left + 1)
    return best_score if best_score != float('inf') else -1

run_test(sliding_window)
```

