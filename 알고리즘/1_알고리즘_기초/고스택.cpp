// title: [3425] 고스택
// link: https://www.acmicpc.net/problem/3425
// 분류 : 자료구조/스택

#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <stdlib.h>

using namespace std;

struct Command {
    string cmd;
    long long param;
};

stack<long long> goStack;
vector<Command> commands;

// Error : stack에 2개 없음. 결과가 10^9을 넘어감
// X를 스택의 가장 위에 저장
bool num(long long param) {
    goStack.push(param);
    return true;
}
// 스택 가장 위의 숫자를 제거
bool pop() {
    if (goStack.size() >= 1) {
        goStack.pop();
        return true;
    } else {
        return false;
    }
}
// 첫 번째 수의 부호를 바꾼다
bool inv() {
    if (goStack.size() >= 1) {
        long long result = -(goStack.top());
        goStack.pop();
        goStack.push(result);
        return true;
    } else {
        return false;
    }
}
// 첫 번째 숫자를 하나 더 스택의 가장 위에 저장한다.
bool dup() {
    if (goStack.size() >= 1) {
        goStack.push(goStack.top());
        return true;
    } else {
        return false;
    }
}
// 첫 번째 숫자와 두 번째 숫자의 위치를 서로 바꾼다.
bool swp() {
    if (goStack.size() >= 2) {
        long long top = goStack.top();
        goStack.pop();
        long long second = goStack.top();
        goStack.pop();
        goStack.push(top);
        goStack.push(second);
        return true;
    } else {
        return false;
    }
}
// 첫 번째 숫자와 두 번째 숫자를 더한다.
bool add() {
    if (goStack.size() >= 2){
        long long top = goStack.top();
        goStack.pop();
        long long second = goStack.top();
        goStack.pop();
        long long result = top + second;
        if(abs(result) > 1000000000) {
            return false;
        }
        goStack.push(result);
        return true;
    } else {
        return false;
    }
}
// 첫 번째 숫자와 두 번째 숫자를 뺀다.
bool sub() {
    if (goStack.size() >= 2){
        long long top = goStack.top();
        goStack.pop();
        long long second = goStack.top();
        goStack.pop();
        long long result = second - top;
        if(abs(result) > 1000000000) {
            return false;
        }
        goStack.push(result);
        return true;
    } else {
        return false;
    }
}
// 첫 번째 숫자와 두 번째 숫자를 곱한다.
bool mul() {
    if (goStack.size() >= 2){
        long long top = goStack.top();
        goStack.pop();
        long long second = goStack.top();
        goStack.pop();
        long long result = top * second;
        if(abs(result) > 1000000000) {
            return false;
        }
        goStack.push(result);
        return true;
    } else {
        return false;
    }
}
// 첫 번째 숫자로 두 번째 숫자를 나눈 몫을 저장한다.
bool div() {
    if (goStack.size() >= 2){
        long long top = goStack.top();
        goStack.pop();
        long long second = goStack.top();
        goStack.pop();
        if (top == 0) return false;
        long long result = abs(second) / abs(top);
        if (top < 0) {
            if (second > 0) {
                result = - result;
            }
        } else {
            if (second < 0) {
                result = - result;
            } 
        }
        if(abs(result) > 1000000000) {
            return false;
        }
        goStack.push(result);
        return true;
    } else {
        return false;
    }
}
// 첫 번째 숫자로 두 번째 숫자를 나눈 나머지를 저장한다.
bool mod() {
    if (goStack.size() >= 2){
        long long top = goStack.top();
        goStack.pop();
        long long second = goStack.top();
        goStack.pop();
        if (top == 0) return false;
        long long result;
        if (second < 0) {
            result = abs(second) % abs(top);
            result = -result;
        } else {
            result = abs(second) % abs(top);
        }
        if(abs(result) > 1000000000) {
            return false;
        }
        goStack.push(result);
        return true;
    } else {
        return false;
    }
}

int main()
{
    
    ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

    // freopen("input.txt", "r", stdin);

    while (true) {
        while (true) {
            string input;
            cin >> input;

            if (input == "QUIT") {
                return 0;
            } else if (input == "END") {
                break;
            } else if (input == "NUM") {
                long param;
                cin >> param;
                Command temp = {input, param};
                commands.push_back(temp);
            } else {
                Command temp = {input, 0};
                commands.push_back(temp);
            }
        }

        int numLength;
        cin >> numLength;
        long input;
        for (int i = 0; i < numLength; i++) {
            cin >> input;
            goStack.push(input);

            bool success = true;

            for (Command command : commands) {
                if (success == false) {
                    break;
                }
                if (command.cmd == "NUM") {
                    success = num(command.param);
                } else if (command.cmd == "POP") {
                    success = pop();
                } else if (command.cmd == "INV") {
                    success = inv();
                } else if (command.cmd == "DUP") {
                    success = dup();
                } else if (command.cmd == "SWP") {
                    success = swp();
                } else if (command.cmd == "ADD") {
                    success = add();
                } else if (command.cmd == "SUB") {
                    success = sub();
                } else if (command.cmd == "MUL") {
                    success = mul();
                } else if (command.cmd == "DIV") {
                    success = div();
                } else if (command.cmd == "MOD") {
                    success = mod();
                } 
            }
            if(success == false || goStack.size() != 1) {
                cout << "ERROR" << endl;
            } else {
                cout << goStack.top() << endl;
            }
            while( !goStack.empty() ) goStack.pop();
        }
        commands.clear();
        cout << endl;
    }
    return 0;
}
