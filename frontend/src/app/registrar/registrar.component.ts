import { Component, OnInit } from '@angular/core';
import { IRegistrar } from '../registrar.service';
import { ActivatedRoute } from '@angular/router';
import { Router}   from '@angular/router';
import { RegistrarService } from "../registrar.service";
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
  
  correoC : '',
  nombreC : '',
  telefonoC : '',
  estadoC : '',
  ciudadC : '',
  coloniaC : '',
  cpC : '',
  calleC : '',
  numeroC : 0
  }
  dataV = {
  
    correoV : '',
    nombreV : '',
    telefonoV : '',
    estadoV : '',
    ciudadV : '',
    coloniaV : '',
    cpV : '',
    calleV : '',
    numeroV : 0,
    tarjetaV : ''
    }







  constructor(private _route:ActivatedRoute, private _registrarService: RegistrarService, private router: Router) { }

  ngOnInit(): void {
  }

  submit(){
    console.log(this.dataC)
    this._registrarService.registrarC(this.dataC).subscribe(response => {
      this.correoDatos = response.msg;
      if(this.correoDatos == 'error_correo'){
        Swal.fire({icon:'error',
                  title:'Error!!',
                  text:' Por favor de ingresar un correo valido'})
      }
      if(this.correoDatos == 'correo_registrado'){
        Swal.fire({icon:'error',
        title:'Error!!',
        text:'Correo ya registrado, por favor ingrese otro o inicia sesión'})
      }
      if(this.correoDatos == 'success'){
        Swal.fire({icon : 'success',
                  title : '¡Exito!',
                  text : 'Usuario registrado correctamente, te enviamos un correo a}'+ this.dataC.correoC})
        this.router.navigate(['/']);
      }

      console.log(response)
      
    
    }, error => { console.log(error)
    if(error.status == 400){
      Swal.fire('Usuario o contraseña incorrectos')
    }
    
    } )

  }

  submitV(){
    this._registrarService.registrarV(this.dataV).subscribe(response => {
      this.correoDatos = response.msg;
      if(this.correoDatos == 'error_correo'){
        Swal.fire({icon:'error',
        title:'Error!!',
        text:' Por favor de ingresar un correo valido'})
      }
      if(this.correoDatos == 'correo_registrado'){
        Swal.fire({icon:'error',
        title:'Error!!',
        text:'Correo ya registrado, por favor ingrese otro o inicia sesión'})
      }
      if(this.correoDatos == 'success'){
        Swal.fire({icon : 'success',
        title : '¡Exito!',
        text : 'Usuario registrado correctamente, te enviamos un correo a'+ this.dataV.correoV})
        this.router.navigate(['/l']);
      }
      console.log(response)
    
    })


  }


}
