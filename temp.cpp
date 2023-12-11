#include<bits/stdc++.h>
using namespace std;
 
#define ll int64_t
#define endl "\n"
const ll mod=998244353;
const ll INF = 1e16;
#define all(x) x.begin(),x.end()
 


int solve1(int warehouse_nodes, vector<int>warehouse_from, vector<int>warehouse_to){

    vector<int>deg(warehouse_nodes+1);
    vector<set<int>>adj(warehouse_nodes+1);
    for(int i=0;i<warehouse_from.size();i++){
        deg[warehouse_from[i]]++;
        deg[warehouse_to[i]]++;
        adj[warehouse_from[i]].insert(warehouse_to[i]);
        adj[warehouse_to[i]].insert(warehouse_from[i]);
    }

    set<pair<int,int>>mt;
    for(int i=1;i<=warehouse_nodes;i++){
        mt.insert({deg[i],i});
    }
    int ans=0;
    while(1){
        if(mt.empty() or (*mt.begin()).first>1){
            break;
        }
        auto p = *mt.begin();
        int v=p.second;
        int d=p.first;

        mt.erase(mt.begin());

        if(d==0){
            ans++;
            
        }else{
            int u=*(adj[v].begin());
            mt.erase(mt.find({deg[u], u}));
            deg[u]--;
            mt.insert({deg[u],u});
            adj[u].erase(v);
            adj[v].erase(u);
            deg[v]--;              
        }
    }
    return ans;
}

vector<vector<int>>adj;
int ans=0;
void dfs(int v, int p, vector<int>cnt, vector<int>&initial, vector<int>&expected){
    int curr_val = cnt[initial[v]];
    if(curr_val!=expected[v]){
        ans++;
        if(curr_val==1){
            cnt[0]=1;
        }else{
            cnt[1]=0;
        }
    }
    for(auto u:adj[v]){
        if(u!=p){
            dfs(u,v,cnt,initial,expected);
        }
    }
}


int solve(int tree_nodes,vector<int>tree_from, vector<int>tree_to, vector<int>initial, vector<int>expected){
    ans=0;
    adj=vector<vector<int>>(tree_nodes+1);
    for(int i=0;i<tree_to.size();i++){
        adj[tree_from[i]].push_back(tree_to[i]);
        adj[tree_to[i]].push_back(tree_from[i]);
    }
    dfs(0,-1,{0,1},initial,expected);
    return ans;
}
 
class A{
    public:
    char c;
    long long d;
};

int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL);cout.tie(NULL);
    int t=1;
    A* a = new A();

    cout<<sizeof(A)<<endl;

    // cin>>t;
   
    return 0; 
}