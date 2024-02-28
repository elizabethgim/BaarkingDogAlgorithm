/**
 * [백준, 10828] 스택
 * 출처: https://st-lab.tistory.com/175
 * 428ms
 * else가 빠른 듯, else를 붙이면 420ms
 */
package bj10828;

import java.util.*;

public class Main{
    public static int[] stack;
    public static int size = 0;

    public static void push(int item){
        stack[size] = item;
        size++;
    }

    public static int pop(){
        if(size == 0){
            return -1;
        }

        int res = stack[size-1];
        stack[size-1] = 0;
        size--;
        return res;
    }

    public static int size(){
        return size;
    }

    public static int empty(){
        if(size==0){
            return 1;
        }
        return 0;
    }

    public static int top(){
        if(size==0){
            return -1;
        }

        return stack[size-1];
    }


    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        int N = in.nextInt();

        stack = new int[N];

        for(int i=0;i< N;i++){
            String str = in.next();

            switch(str){
                case "push":
                    push(in.nextInt());
                    break;
                case "pop":
                    sb.append(pop()).append('\n');
                    break;
                case "size":
                    sb.append(size()).append('\n');
                    break;
                case "top":
                    sb.append(top()).append('\n');
                    break;
                case "empty":
                    sb.append(empty()).append('\n');
                    break;
            }
        }

        System.out.println(sb);
    }
}