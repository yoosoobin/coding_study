function solution(s) {
    let stack = [];
    let answer = 0;
    
    for(let i = 0; i < s.length; i ++){
    stack.push(s[i]);
    
    const same = stack.filter((item) => item === stack[0]);
    const notsame = stack.filter((item) => item !== stack[0]);
    
    if(same.length === notsame.length){
        answer += 1;
        stack = [];
    }
}
    
    if(stack.length !== 0) {
        answer +=1;
    }
    return answer;
}
