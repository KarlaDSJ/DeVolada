
import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';
import Swal from 'sweetalert2';
import { MetodoPagoService } from '../metodo-pago.service';
import { CarritoService } from '../carrito.service';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-metodo-pago',
  templateUrl: './metodo-pago.component.html',
  styleUrls: ['./metodo-pago.component.css']
})

export class MetodoPagoComponent implements OnInit {

  // Cambiar por la consulta a la base
  comprador = ""
  // comprador = "zogilvie1w@ezinearticles.com"
  direccionEntrega = -2;
  idCarrito = -1;

  listaT = [];
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

    let fechaCad = '20' + f.value.anio + '-' + f.value.mes + '-28'

    this._metodopagoService.agregarTar(this.comprador, f.value.numero, f.value.cvv + '', f.value.dueno, fechaCad)
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
  async obtenerTar(f: NgForm) {
    this.vtar = true;
    if (f.invalid) {
      return;
    }

    this.tar = f.value.tarElig;
    // Crear la compra    
    let tarElig = '' + this.tar;
    try {
      let [total, tarjeta] = await Promise.all([
        this._carritoService.obtenerTotal(this.idCarrito),
        this._metodopagoService.obtenerTarjeta(this.comprador, tarElig)
      ]);
      console.log("Total", total);
      this.finalizarCompra(total, tarjeta.tarjeta);
    } catch (error) {
      Swal.fire({
        title: 'Ocurrió un error al finalizar tu compra',
        text: 'Hubo un error con tu tarjeta y tu total. Inténtalo más tarde' + error.message,
        icon: 'error'
      })
    }
  }


  async finalizarCompra(total, tarjeta) {
    let idCompra = 0;
    await this._carritoService.finalizarCompra(this.comprador, this.direccionEntrega, tarjeta, total)
      .then(
        data => {
          idCompra = data.idCompra
          this.router.navigate(['/compra-finalizada', idCompra])
        },
        error => {
          Swal.fire({
            title: 'Ocurrió un error al finalizar la compra',
            icon: 'error'
          })
        }
      )
  }

  // Cancela la compra y redirige a la página de inicio
  cancelar() {
    this.router.navigate(['/inicio'])
  }

  constructor(private router: Router,
    private _metodopagoService: MetodoPagoService,
    private _carritoService: CarritoService,
    private cookie: CookieService) { }

  async ngOnInit(): Promise<void> {
    this.comprador = this.cookie.get('token_access');
    try {
      let [datos, tarjetas] = await Promise.all([
        this._carritoService.obtenerCarrito(this.comprador),
        this._metodopagoService.obtenerTarjetas(this.comprador)
      ])
      this.idCarrito = Number(datos.msg)
      this.listaT = tarjetas.map(x => ({
        tipo: this.tipoT(x.tarjeta),
        numero: x.tarjeta
      }))
    } catch (error) {
      Swal.fire({
        icon: 'error',
        title: 'Carrito no encontrado'
      })
    }

    this.direccionEntrega = Number(localStorage.getItem('devoladaIdDir'))
  }

}