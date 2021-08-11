import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { DireccionCompradorService } from '../direccion-comprador.service';
import Swal from 'sweetalert2';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-direccion',
  templateUrl: './direccion.component.html',
  styleUrls: ['./direccion.component.css']
})

export class DireccionComponent implements OnInit {

  correo = ""
  listaDir = [];
  validez = false;
  vdir = false;
  direccionEntrega = -1;

  /**
   * Formato en el que se muestra una dirección 
   * @param i índica de la lista de direcciones
   * @returns cadena de texto con la información de una dirección
   */
  formato(i: number): string {
    let dir = "";
    dir = this.listaDir[i].calleNum + ", " + this.listaDir[i].colonia + ", " + this.listaDir[i].ciudad + ", " +
      this.listaDir[i].estado + ", " + this.listaDir[i].cp;
    return dir;
  }

  /**
   * Valida los campos del formulario y la agrega a la base
   * y a la lista en caso de ser válida. En caso contrario
   * muestra un mensaje de error.
   * @param f formulario en el que se registra la dirección
   */
  validarDir(f: NgForm) {

    this.validez = true;
    if (f.invalid) {
      return;
    }

    this._direccionService.registrarDireccion(this.correo, f.value.estado, f.value.ciudad, f.value.colonia, f.value.cp, f.value.calle, f.value.num)
      .subscribe(data => {
        Swal.fire({
          title: 'Se agregó tu dirección',
          text: data.idDir + "",
          icon: 'success'
        })
        this.listaDir.push({
          calleNum: f.value.calle + " " + f.value.num,
          colonia: f.value.colonia,
          ciudad: f.value.ciudad,
          estado: f.value.estado,
          cp: Number(f.value.cp),
          idDir: data.idDir
        });

      },
        error => {
          Swal.fire({
            title: 'No se puede agregar',
            text: error.error.msg,
            icon: 'error'
          })
        })
  }

  /**
   * Obtiene la dirección y crea la nueva vista metodo-pago
   * @param f formulario en el que se muestran las direcciones   
   */
  obtenerDir(f: NgForm) {
    this.vdir = true;
    if (f.invalid) {
      return;
    }
    // Pasarsela a metodo-pago 
    localStorage.setItem('devoladaIdDir', f.value.dirElig + '')
    this.router.navigate(['/metodo-pago'])
  }

  /**
   * Cancela la compra y redirige a la página de inicio
   */
  cancelar() {
    this.router.navigate(['/inicio'])
  }

  constructor(private router: Router,
    private _direccionService: DireccionCompradorService,
    private cookie: CookieService) { }

  ngOnInit(): void {
    this.correo = this.cookie.get('token_access');
    this._direccionService.obtenerDirecciones(this.correo)
      .subscribe(data => {
        this.listaDir = data.map(x => ({
          calleNum: x.calle + " " + x.numero,
          colonia: x.colonia,
          ciudad: x.ciudad,
          estado: x.estado,
          cp: x.cp,
          idDir: x.idDir
        }))

      })
  }

}



