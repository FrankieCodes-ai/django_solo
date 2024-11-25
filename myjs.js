    function press(){


        counter += 1
        const text = document.getElementById("myText")
        const intext = document.getElementById("in").value 

        if( counter <10 ){
            text.innerHTML = intext
        }else{
            text.innerHTML = counter

        }
       

    }