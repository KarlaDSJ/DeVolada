
import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-metodo-pago',
  templateUrl: './metodo-pago.component.html',
  styleUrls: ['./metodo-pago.component.css']
})

export class MetodoPagoComponent implements OnInit {

  // Cambiar por la consulta a la base
  listaT=[
    {tipo: "Visa", numero: "4975 4536 7895 1234",mes_exp: 10, anio_exp : 23, cvv: 123, nombre: "Keth bb"}, // Las visa comienzan con 4
    {tipo: "MasterCard", numero: "5975 4536 7895 1895", mes_exp: 10, anio_exp : 23, cvv: 123, nombre: "Keth bb"} // Mastercard comienzan con 5
  ];

  valida = false;
  vtar = false;
  tar="";

  // Formato en el que se muestra una tarjeta
  formato(i:number) : string {
    let tar = "";
    tar = this.listaT[i].tipo+" terminada en "+ this.listaT[i].numero.substr(-4,4);
    return tar;
  }

  // Validar una tarjeta
  validarTar(f:NgForm){
    console.log("Entré");    
    this.valida= true;

    if (f.invalid) {
      console.log("Fallé",f);      
      return;
    } 

    this.listaT.push({
      tipo: this.tipoT(f.value.numero),
      numero: f.value.numero,
      mes_exp: f.value.mes,
      anio_exp: f.value.anio,
      cvv : Number(f.value.cvv),
      nombre: f.value.dueno      
    });       
  }

  // Indica si una tarjeta es visa, mastercard o desconocida
  tipoT(num:string): string{
    let p= num.substr(0,1);
    if (p=="4") {
      return "Visa";
    } else 
      return "MasterCard";    
  }

  obtenerTar(f:NgForm){
    this.vtar = true;
    if(f.invalid){
      return;
    }
    
    this.tar= f.value.tarElig;
    // console.log(f.value.tarElig);
    this.router.navigate([ '/compra-finalizada' ])

  }

  // Cancela la compra y redirige a la página de inicio
  cancelar(){
    this.router.navigate([ '/inicio' ])
  }

  constructor(private router: Router) { }

  ngOnInit(): void {
  }

}