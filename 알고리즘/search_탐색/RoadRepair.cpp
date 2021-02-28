// title: Road Repair
// 분류: dfs
/* 문제: A number of points along the highway are in need of repair. An equal number of crews are available, stationed at various points along the highway.
They must move along the highway to reach an assigned point. 
Given that one crew must be assigned to each job, what is the minimum total amout of distance traveled by all crews before they can begin work?

For example, given crews at points {1, 3, 5} and required repairs at {3, 5, 7},
one possible minimum assignment would be {1->3, 3->5, 5->7} for a total of 6 units traveled.

Function Description
Complete the function getMinCost in the editor below.
The function should return the minimum possible total distance traveled as an integer.
*/
#include <bits/stdc++.h>
#include <algorithm>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);



/*
 * Complete the 'getMinCost' function below.
 *
 * The function is expected to 
 * return a LONG_INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY crew_id
 *  2. INTEGER_ARRAY job_id
 */


long answer = 0;

void dfs(int c_id, int j_id, vector<int> crew_id, vector<int> job_id, vector<bool> visited, long dist) {

    visited[j_id] = true;
    dist += abs(crew_id[c_id] - job_id[j_id]);
    c_id++;
    if (c_id == crew_id.size()) {
        answer = min(answer, dist);
    } else {
        for (int i=0; i<job_id.size(); i++) {
            if (!visited[i]) {
                dfs(c_id, i, crew_id, job_id, visited, dist);
            }
        }
    }
}

long getMinCost(vector<int> crew_id, vector<int> job_id) {
    vector<bool> visited(job_id.size(), false);
    sort(crew_id.begin(), crew_id.end());
    sort(job_id.begin(), job_id.end());
    for (int i=0; i<crew_id.size(); i++) {
        answer += abs(crew_id[i] - job_id[i]);
    }
    dfs(0, 0, crew_id, job_id, visited, 0);
    return answer;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string crew_id_count_temp;
    getline(cin, crew_id_count_temp);

    int crew_id_count = stoi(ltrim(rtrim(crew_id_count_temp)));

    vector<int> crew_id(crew_id_count);

    for (int i = 0; i < crew_id_count; i++) {
        string crew_id_item_temp;
        getline(cin, crew_id_item_temp);

        int crew_id_item = stoi(ltrim(rtrim(crew_id_item_temp)));

        crew_id[i] = crew_id_item;
    }

    string job_id_count_temp;
    getline(cin, job_id_count_temp);

    int job_id_count = stoi(ltrim(rtrim(job_id_count_temp)));

    vector<int> job_id(job_id_count);

    for (int i = 0; i < job_id_count; i++) {
        string job_id_item_temp;
        getline(cin, job_id_item_temp);

        int job_id_item = stoi(ltrim(rtrim(job_id_item_temp)));

        job_id[i] = job_id_item;
    }

    long result = getMinCost(crew_id, job_id);

    fout << result << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
