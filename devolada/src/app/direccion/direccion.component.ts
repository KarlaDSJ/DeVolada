import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-direccion',
  templateUrl: './direccion.component.html',
  styleUrls: ['./direccion.component.css']
})

export class DireccionComponent implements OnInit {

  // Cambiar por la consulta a la base de datos
  listaDir = [
    {calleNum:"Churbusco 152", colonia: "Metropolitana", ciudad: "Nezahualcoyotl",
    estado: "México", cp: 78562 },
    {calleNum:"Matemáticas 336", colonia: "Centro", ciudad: "Benito Juárez",
    estado: "Ciudad de México", cp: 94523 }
  ];
  
  validez=false;

  // Formato en el que se muestra una dirección 
  formato(i:number) : string {
    let dir = "";
    dir = this.listaDir[i].calleNum+", "+ this.listaDir[i].colonia+", "+this.listaDir[i].ciudad+", "+
    this.listaDir[i].estado+", "+this.listaDir[i].cp;
    return dir;
  }
  
  // Valida los campos del formulario 
  validarDir(f:NgForm){
    this.validez= true;
    if (f.invalid) {
      return;
    } 

    this.listaDir.push({
      calleNum: f.value.calle + " "+ f.value.num,
      colonia: f.value.colonia,
      ciudad: f.value.ciudad,
      estado: f.value.estado,
      cp: Number(f.value.cp)
    });       
  }

  constructor() { }

  ngOnInit(): void {    
  }

}



