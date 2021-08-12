import { Component, OnInit } from '@angular/core';
import { IRegistrar } from '../../services/registrar.service';
import { Router } from '@angular/router';
import { RegistrarService } from "../../services/registrar.service";
import { CarritoService } from '../../services/carrito.service';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-registrar',
  templateUrl: './registrar.component.html',
  styleUrls: ['./registrar.component.css']
})
/**
 * Clase del componente Registrar para que el usuario se pueda registrar a nuestro sistema
 */
export class RegistrarComponent implements OnInit {
  
  registrar: IRegistrar; //interfaz

  correoDatos = ''; //para verificar si el correo

  //los datos de comprador

  dataC = {
    correoC: '',
    nombreC: '',
    telefonoC: '',
    estadoC: '',
    ciudadC: '',
    coloniaC: '',
    cpC: '',
    calleC: '',
    numeroC: 0
  }

  //los datos del vendedor

  dataV = {
    correoV: '',
    nombreV: '',
    telefonoV: '',
    estadoV: '',
    ciudadV: '',
    coloniaV: '',
    cpV: '',
    calleV: '',
    numeroV: 0,
    tarjetaV: ''
  }

  /**
   * Contructor de la clase
   * @param _registrarService 
   * @param router la ruta por si redirigimos al usuario a otra pagina
   * @param _carritoService 
   */

  constructor(
    private _registrarService: RegistrarService, 
    private router: Router,
    private _carritoService: CarritoService) { }

  /**
   * Otro constructor de la clase
   */  
  
  ngOnInit(): void {
  }

  /**
   * Función que sube los datos del comprador al observable que es el servicio de registrar ademas de verificar
   * que los datos son correctos
   */

  submit() {
    this._registrarService.registrarC(this.dataC).subscribe(async response => {
      this.correoDatos = response.msg;
      if (this.correoDatos == 'error_correo') {
        Swal.fire({
          icon: 'error',
          title: 'Error!!',
          text: ' Por favor de ingresar un correo valido'
        })
      }
      if (this.correoDatos == 'correo_registrado') {
        Swal.fire({
          icon: 'error',
          title: 'Error!!',
          text: 'Correo ya registrado, por favor ingrese otro o inicia sesión'
        })
      }
      if (this.correoDatos == 'success') {
        Swal.fire({
          icon: 'success',
          title: '¡Exito!',
          text: 'Usuario registrado correctamente, te enviamos un correo a ' + this.dataC.correoC
        })
        // Se crea su carrito
        let carrito = -1;
        try {
          let my_carrito =  await this._carritoService.crearCarrito();
          carrito = Number (my_carrito.idCarrito)  
          let asignar = await this._carritoService.asignarCarrito(carrito, this.dataC.correoC)                  
          console.log(asignar)
        } catch (error) {
          Swal.fire({
            icon: 'error',
            title: 'Error!!',
            text: 'No se pudo crear tu carrito :('
          })
        }
        this.router.navigate(['/']);
      }
    }, error => {
      console.log(error)
      if (error.status == 400) {
        Swal.fire('Usuario o contraseña incorrectos')
      }
    })
  }

  /**
   * Función que sube los datos del vendedor al observable que es el servicio de registrar ademas de verificar
   * que los datos son correctos
   */

  submitV() {
    this._registrarService.registrarV(this.dataV).subscribe(response => {
      this.correoDatos = response.msg;
      if (this.correoDatos == 'error_correo') {
        Swal.fire({
          icon: 'error',
          title: 'Error!!',
          text: ' Por favor de ingresar un correo valido'
        })
      }
      if (this.correoDatos == 'correo_registrado') {
        Swal.fire({
          icon: 'error',
          title: 'Error!!',
          text: 'Correo ya registrado, por favor ingrese otro o inicia sesión'
        })
      }
      if (this.correoDatos == 'success') {
        Swal.fire({
          icon: 'success',
          title: '¡Exito!',
          text: 'Usuario registrado correctamente, te enviamos un correo a  ' + this.dataV.correoV
          
        })
        this.router.navigate(['/']);
      }
    })
  }
}