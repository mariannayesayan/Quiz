# Quiz
Queue has a first in first out (FIFO) principle, which means that you have a group of objects, where you can insert and remove items. the main features of the queue is that it does have specific number of elements in it, but the capacity is not limited. So, queue works in the following way: when you insert some object you have to remove it firstly. And in Queue we have only 2 operations : Enqueue and Dequeue. Enqueue places an element in the last place, while dequeue removes an element that was put first.
The complexity of Queue is always O(1). As we know that element will be added from the “top” and removed from the “end” then it requires only a one step.
A good example of queue will be when you take a ticket and wait for your turn. So, a person who comes first will get his ticket first, and a person who comes late will take his ticket at the end.
The code:
In the code it is needed to use array as a type of storing the items which means that the queue has limited length. So, it can also be empty or full. If it will be empty then any element will not be able to be removed and in case it will be full no element can be added.

I have made a class queue which has items placed in an array. Then I defined methods for the queue which are is_empty(to check whether it is empty or not), size (that counts the length of the queue).

Also, I have added enqueue and dequeue. In the least ones I wrote a code that will check whether elements can be added or removed accordingly.
