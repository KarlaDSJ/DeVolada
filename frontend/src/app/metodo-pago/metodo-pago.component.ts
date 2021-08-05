
import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import Swal from 'sweetalert2';
import { MetodoPagoService } from '../metodo-pago.service';

@Component({
  selector: 'app-metodo-pago',
  templateUrl: './metodo-pago.component.html',
  styleUrls: ['./metodo-pago.component.css']
})

export class MetodoPagoComponent implements OnInit {

  comprador = "kethrim.tradmateos@gmail.com"
  direccionEntrega = -2;
  // Cambiar por la consulta a la base
  listaT = [
    // {tipo: "Visa", numero: "4975 4536 7895 1234",mes_exp: 10, anio_exp : 23, cvv: 123, nombre: "Keth bb"}, // Las visa comienzan con 4
    // {tipo: "MasterCard", numero: "5975 4536 7895 1895", mes_exp: 10, anio_exp : 23, cvv: 123, nombre: "Keth bb"} // Mastercard comienzan con 5
  ];

  valida = false;
  vtar = false;
  tar = "";



  // Formato en el que se muestra una tarjeta
  formato(i: number): string {
    let tar = "";
    tar = this.listaT[i].tipo + " terminada en " + this.listaT[i].numero.substr(-4, 4);
    return tar;
  }

  // Validar una tarjeta
  validarTar(f: NgForm) {
    console.log("Entré");
    this.valida = true;

    if (f.invalid) {
      console.log("Fallé", f);
      return;
    }

    let fechaCad = '20'+f.value.anio + '-' + f.value.mes + '-28'

    this._metodopagoService.agregarTar(this.comprador, f.value.numero, f.value.cvv+'', f.value.dueno, fechaCad)
      .subscribe(
        data => {
          Swal.fire({
            title: 'Se agregó tu tarjeta',
            icon: 'success'
          })
        },
        error => {
          Swal.fire({
            title: 'Ocurrió un error',
            text: 'Inténtalo más tarde',
            icon: 'error'
          })
        })

    this.listaT.push({
      tipo: this.tipoT(f.value.numero),
      numero: f.value.numero
    });
  }

  // Indica si una tarjeta es visa, mastercard o desconocida
  tipoT(num: string): string {
    let p = num.substr(0, 1);
    if (p == "4") {
      return "Visa";
    } else
      return "MasterCard";
  }

  // Obtiene el método de pago elegido 
  // Redirecciona a la info de la compra
  obtenerTar(f: NgForm) {
    this.vtar = true;
    if (f.invalid) {
      return;
    }

    this.tar = f.value.tarElig;
    // Crear la compra
    let idCompra = 0;

    // Mostrar la compra
    this.router.navigate(['/compra-finalizada', idCompra])
    localStorage.removeItem('devoladaIdDir')

  }

  // Cancela la compra y redirige a la página de inicio
  cancelar() {
    this.router.navigate(['/inicio'])
  }

  constructor(private router: Router, private _metodopagoService: MetodoPagoService) { }

  ngOnInit(): void {
    this._metodopagoService.obtenerTarjetas(this.comprador)
      .subscribe(data => {
        this.listaT = data.map(x => ({
          tipo: this.tipoT(x.tarjeta),
          numero: x.tarjeta
        }))
      })
    this.direccionEntrega = Number(localStorage.getItem('devoladaIdDir'))
  }

}