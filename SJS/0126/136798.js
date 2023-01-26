function solution(number, limit, power){
    var answer = 0;
    
    // 약수 담을 변수 선언
    let count = 0;
    
    for(let i=1; i<=number; i++){
        count = 0; 
        
        // 약수 구하기
        // 구할 숫자의 반절까지만 나눠보면 된다. 
        // 왜냐면 약수는 구할 숫자, 즉 본인을 제외하고 대상의 1/2보다 큰 숫자가 나올 수 없기때문
        for ( let j = 1; j <= i/2; j++){
            if( i%k === 0){
                count += 1;
            }
        }
        
        // 본인을 뺐으므로 +1 
        count += 1;
        
        // limit 조건 
        if(count > limit) {
            answer += power;
        }
        
        else{
            answer += count;
        }
        
    }
    return answer;
}
