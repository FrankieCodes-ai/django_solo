function update_cost(){


    let arrive = document.getElementById('id_hotel_date_arrive').ariaValueMax
    let leave = document.getElementById('id_hotel_date_leave').value


    arrive = new Date(arrive)
    leave = new Date(leave)
    diff = leave.getTime() - arrive.getTime();
    days = Math.round(Math.abs(diff/(1000*60*60*24)));


    if (String(days) == "NaN"){
        let price = document.getElementById('hotel_output')
        price.innerHTML = "Hotel Cost: Dates Not Chosen"
    }else{

        let total = parseInt(adults.value) * 60
                    + parseInt(children.value) * 25

        total = total * days


        let price = document.getElementById('hotel_output')
        price.innerHTML = "Hotel cost: £" + String(total)


    }
}

let adults = document.getElementById("id_hotel_adults");
adults.addEventListener("change", update_cost)
let children = document.getElementById("id_hotel_children");
adults.addEventListener("change", update_cost)
