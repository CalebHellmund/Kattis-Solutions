// Problem: Climbing Worm
// Link: https://open.kattis.com/problems/climbingworm
// Difficulty: Easy


#include <iostream>

using namespace std;

int main (){
    int a, b, h;
    int count = 0;
    int position = 0;
    
    cin >> a >> b >> h;
    
    while (position <= h){
        position += a;
        count++;
        if(position >= h){
            break;
        }
        position -=b;
    }
    cout << count << endl;
    
    return 0;
}