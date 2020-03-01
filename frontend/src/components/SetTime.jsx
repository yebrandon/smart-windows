import React from "react";
import "./Layout.css";
import Settings from "./Settings";
import { Link } from 'react-router-dom';
import Toggle from './Toggle';
import Layout from './Layout';


var num = [];

function addToArray( NumToAdd){
    num[num.length]=NumToAdd;
    return 0;
}

class SetTime extends React.Component{
    
    

    render(){
        return(
            <div>
               


                <Link to="/Layout">
                    <button type="button" id = "Back">Back</button>
                </Link>

                <button onclick = {addToArray(0)} type= "button" id = "0">0:00</button>
                <button onclick = {addToArray(1)} type= "button" id = "1">1:00</button>
                <button onclick = {addToArray(2)} type= "button" id = "2">2:00</button>
                <button onclick = {addToArray(3)} type= "button" id = "3">3:00</button>
                <button onclick = {addToArray(4)} type= "button" id = "4">4:00</button>
                <button onclick = {addToArray(5)} type= "button" id = "5">5:00</button>
                <button onclick = {addToArray(6)} type= "button" id = "6">6:00</button>
                <button onclick = {addToArray(7)} type= "button" id = "7">7:00</button>
                <button onclick = {addToArray(8)} type= "button" id = "8">8:00</button>
                <button onclick = {addToArray(9)} type= "button" id = "9">9:00</button>
                <button onclick = {addToArray(10)} type= "button" id = "10">10:00</button>
                <button onclick = {addToArray(11)} type= "button" id = "11">11:00</button>
                <button onclick = {addToArray(12)} type= "button" id = "12">12:00</button>
                <button onclick = {addToArray(13)} type= "button" id = "13">13:00</button>
                <button onclick = {addToArray(14)} type= "button" id = "14">14:00</button>
                <button onclick = {addToArray(15)} type= "button" id = "15">15:00</button>
                <button onclick = {addToArray(16)} type= "button" id = "16">16:00</button>
                <button onclick = {addToArray(17)} type= "button" id = "17">17:00</button>
                <button onclick = {addToArray(18)} type= "button" id = "18">18:00</button>
                <button onclick = {addToArray(19)} type= "button" id = "19">19:00</button>
                <button onclick = {addToArray(20)} type= "button" id = "20">20:00</button>
                <button onclick = {addToArray(21)} type= "button" id = "21">21:00</button>
                <button onclick = {addToArray(22)} type= "button" id = "22">22:00</button>
                <button onclick = {addToArray(23)} type= "button" id = "23">23:00</button>
                <button type= "button" id = "finish">finish</button>



            </div>









        )
    }
}
export default SetTime;