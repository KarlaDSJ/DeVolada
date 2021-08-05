import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { DireccionCompradorService } from '../direccion-comprador.service';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-direccion',
  templateUrl: './direccion.component.html',
  styleUrls: ['./direccion.component.css']
})

export class DireccionComponent implements OnInit {

  // Aquí debería usar el correo del comprador actual 
  // duenio = "zogilvie1w@ezinearticles.com"
  duenio = "kethrim.tradmateos@gmail.com"
  
  listaDir = [];
  validez = false;
  vdir = false;
  direccionEntrega = -1;

  // Formato en el que se muestra una dirección 
  formato(i: number): string {
    let dir = "";
    dir = this.listaDir[i].calleNum + ", " + this.listaDir[i].colonia + ", " + this.listaDir[i].ciudad + ", " +
      this.listaDir[i].estado + ", " + this.listaDir[i].cp;
    return dir;
  }

  // Valida los campos del formulario 
  validarDir(f: NgForm) {

    this.validez = true;
    if (f.invalid) {
      return;
    }

    this._direccionService.registrarDireccion(this.duenio, f.value.estado,f.value.ciudad, f.value.colonia, f.value.cp, f.value.calle, f.value.num)
      .subscribe(data => {
        Swal.fire({
          title: 'Se agregó tu dirección',
          text: data.idDir+"",
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
          text: error.error.msg ,
          icon: 'error'
        })
      })   
  }

  // Obtiene la dirección y crea la nueva vista 
  obtenerDir(f: NgForm) {
    this.vdir = true;
    if (f.invalid) {
      return;
    }
    // Pasarsela a metodo-pago 
    // this.direccionEntrega = f.value.dirElig;
    localStorage.setItem('devoladaIdDir', f.value.dirElig+'')
    this.router.navigate(['/metodo-pago'])
  }

  // Cancela la compra y redirige a la página de inicio
  cancelar() {
    this.router.navigate(['/inicio'])
  }

  constructor(private router: Router, private _direccionService: DireccionCompradorService) { }

  ngOnInit(): void {
    this._direccionService.obtenerDirecciones(this.duenio)
      .subscribe(data => {
        this.listaDir = data.map(x => ({
          calleNum: x.calle +" "+ x.numero,
          colonia: x.colonia,
          ciudad: x.ciudad,
          estado: x.estado,
          cp: x.cp,
          idDir: x.idDir
        }))

      })
  }

}



