import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-metodo-pago',
  templateUrl: './metodo-pago.component.html',
  styleUrls: ['./metodo-pago.component.css']
})
export class MetodoPagoComponent implements OnInit {

  listaDir = [
    {calleNum:"Churbusco 152", colonia: "Metropolitana", ciudad: "Nezahualcoyotl",
    estado: "México", cp: 78562 },
    {calleNum:"Matemáticas 336", colonia: "Centro", ciudad: "Benito Juárez",
    estado: "Ciudad de México", cp: 94523 }
  ];

  calleNum ="Churubusco 152";

  // Formato en el que se muestra una dirección 
  formato(i:number) : string {
    let dir = "";
    dir = this.listaDir[i].calleNum+", "+ this.listaDir[i].colonia+", "+this.listaDir[i].ciudad+", "+
    this.listaDir[i].estado+", "+this.listaDir[i].cp;
    return dir;
  }

  guardarDir():void{
    console.log("Nueva dir: ", this.calleNum);    
  }
  

  constructor() { }

  ngOnInit(): void {
  }

}
