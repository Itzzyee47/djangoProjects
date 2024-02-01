
  function auth(){
    
    if(cpass === pass){
        alert('passwords match!!'+ cpass)
        console.log(pass+cpass)
        loginForm.submit()
    }else if(cpass != pass){
        console.log(pass+cpass)
         e.preventDefault();
        alert('passwords donot match!!'+ cpass)
    }
  }