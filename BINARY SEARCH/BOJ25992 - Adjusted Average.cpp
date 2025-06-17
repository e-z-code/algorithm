/*
BOJ25992 - Adjusted Average (https://www.acmicpc.net/problem/25992)

There are N samples.
You can remove at most K samples.
Calculate the possible minimum difference between the adjusted average and goal average.
*/

// TIME COMPLEXITY : O(N^2 log N)

#include <algorithm>
#include <iostream>
#include <iomanip>
#include <set>
#include <vector>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(NULL);


    // 1. TO GET THE INPUT

    long long sample_count, remove_count, goal_average;
    cin >> sample_count >> remove_count >> goal_average;
    
    vector<long long> samples;
    for (int idx = 0; idx < sample_count; idx++) {
        long long element;
        cin >> element;
        samples.push_back(element);
    }
    sort(samples.begin(), samples.end());


    // 2. K <= 2 : BRUTE-FORCE

    long long sample_sum = 0;
    for (int idx = 0; idx < sample_count; idx++) {
        sample_sum += samples[idx];
    }

    double best_error;
    best_error = abs((double) sample_sum / sample_count - goal_average); 

    if (1 <= remove_count) {
        for (int idx = 0; idx < sample_count; idx++) {
            double now_error = abs((double) (sample_sum - samples[idx]) / (sample_count - 1) - goal_average);
            if (now_error < best_error) {
                best_error = now_error;
            }
        }
    }

    if (2 <= remove_count) {
        for (int i = 0; i < sample_count; i++) {
            for (int j = i+1; j < sample_count; j++) {
                double now_error = abs((double) (sample_sum - samples[i] - samples[j]) / (sample_count - 2) - goal_average);
                if (now_error < best_error) {
                    best_error = now_error;
                }
            }
        }
    }


    // 3. K <= 4 : BINARY SEARCH
    
    if (3 <= remove_count) {
        for (int i = 0; i < sample_count; i++) {
            for (int j = i+1; j < sample_count; j++) {
                if (j < sample_count - 1) {

                    long long target = (sample_sum - samples[i] - samples[j]) - goal_average * (sample_count - 3);

                    int left = j+1;
                    int right = sample_count-1;
                    while (left + 1 < right) {
                        int mid = (left + right) / 2;
                        if (target <= samples[mid]) {
                            right = mid;
                        } else {
                            left = mid;
                        }
                    }

                    double left_error = abs((double) (sample_sum - samples[i] - samples[j] - samples[left]) / (sample_count - 3) - goal_average);
                    if (left_error < best_error) {
                        best_error = left_error;
                    }
                    double right_error = abs((double) (sample_sum - samples[i] - samples[j] - samples[right]) / (sample_count - 3) - goal_average);
                    if (right_error < best_error) {
                        best_error = right_error;
                    }
                }
            }
        }
    }

    if (4 <= remove_count) {

        set<long long> key;
        key.insert(samples[0] + samples[1]);

        for (int middle = 2; middle < sample_count; middle++) {

            for (int high = middle+1; high < sample_count; high++) {

                long long target = (sample_sum - samples[middle] - samples[high]) - goal_average * (sample_count - 4);

                auto key_idx = key.lower_bound(target);
                if (key_idx != key.end()) {
                    double now_error = abs((double) (sample_sum - samples[middle] - samples[high] - *key_idx) / (sample_count - 4) - goal_average);
                    if (now_error < best_error) {
                        best_error = now_error;
                    }
                }
                if (key_idx != key.begin()) {
                    double now_error = abs((double) (sample_sum - samples[middle] - samples[high] - *prev(key_idx)) / (sample_count - 4) - goal_average);
                    if (now_error < best_error) {
                        best_error = now_error;
                    }
                }

            }

            for (int low = 0; low < middle; low++) {
                key.insert(samples[low] + samples[middle]);
            }

        }
    }


    // 4. TO SOLVE THE PROBLEM
    
    cout << fixed << setprecision(10) << best_error << '\n';
    return 0;

}