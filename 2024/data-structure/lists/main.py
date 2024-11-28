from linked_list import LinkedList

def main():
    ll = LinkedList()

    print("Initial size: ", len(ll)) # Initial size: 0
    ll.push(24)
    print("New size: ", len(ll)) # New size: 1
    print("List content: ", ll) # List content: 24 ->
    print("Pushing more") 
    ll.push(6)
    ll.push(783)
    print("List content: ", ll) # List content: 783 -> 6 -> 24 -> 
    print("popping...")
    ll.pop()
    print("List content: ", ll) # List content: 6 -> 24 ->
    print("Does list contain 24?") # Yes
    if ll.contains(24):
        print("Yes")
    else:
        print("No")

    print("Deleting 24")
    ll.delete(24)
    print("List content: ", ll) # List content: 6 ->
    print("Pushing another onto end.")
    ll.append(365)
    print("List content: ", ll) # List content: 6 -> 265 ->

    ll.reverse()
    print("Reversed List content: ", ll)

if __name__ == "__main__":
    main()