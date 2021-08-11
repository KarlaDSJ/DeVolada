import { Component, OnInit } from '@angular/core';
import { IRegistrar } from '../../services/registrar.service';
import { ActivatedRoute } from '@angular/router';
import { Router } from '@angular/router';
import { RegistrarService } from "../../services/registrar.service";
import { CarritoService } from '../../services/carrito.service';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-registrar',
  templateUrl: './registrar.component.html',
  styleUrls: ['./registrar.component.css']
})
export class RegistrarComponent implements OnInit {
  registrar: IRegistrar;

  correoDatos = '';
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







  constructor(private _route: ActivatedRoute,
    private _registrarService: RegistrarService, 
    private router: Router,
    private _carritoService: CarritoService) { }

  ngOnInit(): void {
  }

  submit() {
    console.log(this.dataC)
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

      console.log(response)


    }, error => {
      console.log(error)
      if (error.status == 400) {
        Swal.fire('Usuario o contraseña incorrectos')
      }

    })

  }

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
      console.log(response)

    })


  }



}
