/* A two-dimensional matrix, m[0..|s1|,0..|s2|] is used to hold the edit distance values:
m[i,j] = d(s1[1..i], s2[1..j])
m[0,0] = 0

m[i,0] = i,  i=1..|s1|
m[0,j] = j,  j=1..|s2|

m[i,j] = min(m[i-1,j-1]
             + if s1[i]=s2[j] then 0 else 1 fi,
             m[i-1, j] + 1,
             m[i, j-1] + 1 ),  i=1..|s1|, j=1..|s2|

m[,] can be computed row by row. Row m[i,] depends only on row m[i-1,]. 

*/

#include<bits/stdc++.h>


using namespace std;

int condition(char a, char b) {
    if(a == b) return 0;
    return 1;
}

int min(int x,int y,int z)
{
    int k=(x>y)?y:x;
    k=(k>z)?z:k;
    return k;
}

int main() {
    string a, b;
    short m, n, t;
    cin>>t;
    while(t--) {
        cin>>a>>b;
        m = a.length();
        n = b.length();
        short mat[m+1][n+1];

        for(int i = 0; i <= m; i++) mat[i][0] = i;
        for(int j = 1; j <= m; j++) mat[0][j] = j;

        for(int i = 1; i <= m; i++) {
            for(int j = 1; j <= n; j++) {
                mat[i][j] = min(mat[i-1][j]+1, mat[i][j-1]+1, mat[i-1][j-1] + condition(a[i-1], b[j-1]));
            }
        }
        cout<<mat[m][n]<<endl;
    }
}



