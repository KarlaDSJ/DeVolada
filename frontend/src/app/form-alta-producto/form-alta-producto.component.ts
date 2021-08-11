import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { AdminProductoService } from '../admin-producto.service';
import { IadminProducto } from '../admin-producto.service';
import { CookieService } from 'ngx-cookie-service';
import Swal from 'sweetalert2';
import { convertToObject } from 'typescript';

@Component({
  selector: 'app-form-alta-producto',
  templateUrl: './form-alta-producto.component.html',
  styleUrls: ['./form-alta-producto.component.css']
})


export class FormAltaProductoComponent implements OnInit {

  datosProducto = {
    idProducto : 0,
    correo: '',
    nombre: '',
    precio: 0.00,
    disponibles: 1,
    descripcion: '',
    categorias: "",
    imagenes_url: []
  }

  respuesta = { 
    error: null,
    mensaje: null
  }


  // Variable to store shortLink from api response
  shortLink: string = "";
  file: File = null; // Variable para guardar imagen
  loading: boolean = false; // Flag variable
  
  aceptarTerminos = false

  constructor( private _adminService: AdminProductoService, 
               private _cookie: CookieService ){}

  ngOnInit(): void {
    const correo = this._cookie.get('token_access')
    this.datosProducto.correo = correo
  }

  // Acción de click en el botón submit
  submit(){
    console.log(this.datosProducto)
    
    

    // Sube a la BD los datos elementales de la tabla del producto
    this._adminService.daAltaProducto(this.datosProducto).subscribe(respuesta => {

      if ( respuesta.error != undefined){
        this.respuesta.error = respuesta.error 
        this.respuesta.mensaje = respuesta.mensaje
        Swal.fire({icon: 'error', title: 'Ups!', text: this.respuesta.mensaje })
      }
      else {
        this.datosProducto.idProducto = respuesta.idProducto
        Swal.fire({icon: 'success', title: 'Éxito', text: 'Tu producto se ha dado de alta correctamente.'})
      }
    } )  

    // Sube a la BD cada una de las categorias 
    var categorias_json: any = {"categorias": this.datosProducto.categorias }
    this._adminService.agregaCategorias(categorias_json).subscribe(respuesta => {

      
    } )  
  }

  // On file Select
  onChange(event) {
    //this.file = event.target.files[0];
    let files = event.target.files;
    if (files) {
      for (let file of files) {
        let reader = new FileReader();
        reader.onload = (e: any) => {
          this.datosProducto.imagenes_url.push(e.target.result);
        }
        reader.readAsDataURL(file);
      }
    }
  }


  

  // Acción de click en el botón upload
  onUpload() {
    //console.log(this.file);
    this._adminService.upload(this.file).subscribe((respuesta: any) => {
            if (typeof (respuesta) === 'object') {
                // Agregamos la url de la imagen guardada a la lista de imagenes
                this.datosProducto.imagenes_url.push( respuesta.url )
            }
        }
    );
  }


    // Acción de click en el botón upload
    eliminaImg(img_url) {
      
  }

}
