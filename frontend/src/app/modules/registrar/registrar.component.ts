import { Component, OnInit } from '@angular/core';
import { IRegistrar } from '../../services/registrar.service';
import { Router } from '@angular/router';
import { RegistrarService } from "../../services/registrar.service";
import { CarritoService } from '../../services/carrito.service';
import { FormBuilder, FormGroup, Validators} from '@angular/forms';
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

  enviadoC = false;
  enviadoV = false;
  
  //los datos de comprador
  
  correoCesValido = false;
  correoCesVacio = false;
  
  nombreCesVacio = false;
  
  telefonoCesValido = false;
  telefonoCesVacio = false;
  
  estadoCesVacio = false;
  
  
  ciudadCesVacio = false;
  
  
  coloniaCesVacio = false;
  
  cpCesValido = false;
  cpCEsVacio = false;
  
  calleCEsVacio = false;
  
  
  numeroCesValido =  false;
  numeroCesVacio = false;





  correoVesValido = false;
  correoVesVacio = false;
  
  nombreVesVacio = false;
  
  telefonoVesValido = false;
  telefonoVesVacio = false;
  
  estadoVesVacio = false;
  
  
  ciudadVesVacio = false;
  
  
  coloniaVesVacio = false;
  
  cpVesValido = false;
  cpVEsVacio = false;
  
  calleVEsVacio = false;
  
  
  numeroVesValido =  false;
  numeroVesVacio = false;
  
  tarjetaEsVacia = false;
  tarjetaEsValida = false;
  
  
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
    private _carritoService: CarritoService,
    public fb: FormBuilder) { 
      
      
      this.myFormR = this.fb.group({
      correoC : ['',[Validators.required, Validators.email]],
      nombreC : ['',[Validators.required,Validators.minLength(2)]],
      telefonoC : ['', [Validators.required, Validators.pattern("^[0-9]*$")]],
      estadoC : ['', [Validators.required]],
      ciudadC : ['', [Validators.required]],
      coloniaC : ['', [Validators.required]],
      cpC : ['', [Validators.required, Validators.min(1000), Validators.max(99999)]],
      calleC : ['',[Validators.required]],
      numeroC : ['', [Validators.required, Validators.pattern('^[0-9]+$')]],
      
      correoV : ['',[Validators.required, Validators.email]],
      nombreV : ['',[Validators.required]],
      telefonoV : ['', [Validators.required, Validators.pattern('^[0-9]+$')]],
      estadoV : ['', [Validators.required]],
      ciudadV : ['', [Validators.required]],
      coloniaV : ['', [Validators.required]],
      cpV : ['', [Validators.required , Validators.min(1000), Validators.max(99999) ]  ],
      calleV : ['',[Validators.required]],
      numeroV : ['', [Validators.required, Validators.pattern('^[0-9]+$')]],
      tarjeta : ['', [Validators.required, Validators.pattern('^[0-9]{16}$'), Validators.minLength(16), Validators.maxLength(16) ]]
      
      })
    }
    
    
    /**
     * Otro constructor de la clase
     */  
    
    ngOnInit(): void {
      
    }
    
    /**
     * Función que sube los datos del comprador al observable que es el servicio de registrar ademas de verificar
     * que los datos son correctos
     */
    
    myFormR: FormGroup;
    submit() {
      this.enviadoC = true;

      this.correoCesVacio = this.myFormR.get('correoC').hasError('required')
      this.correoCesValido = !this.myFormR.get('correoC').hasError('email')
      
      this.nombreCesVacio = this.myFormR.get('nombreC').hasError('required')
      
      
      this.telefonoCesVacio = this.myFormR.get('telefonoC').hasError('required')
      this.telefonoCesValido = !this.myFormR.get('telefonoC').hasError('pattern')

     

    this.estadoCesVacio = this.myFormR.get('estadoC').hasError('required') 
    
    this.ciudadCesVacio = this.myFormR.get('ciudadC').hasError('required') 

    
    this.coloniaCesVacio = this.myFormR.get('coloniaC').hasError('required')
    
    this.cpCEsVacio = this.myFormR.get('cpC').hasError('required')
 
    
    this.cpCesValido = !this.myFormR.get('cpC').hasError('min') && !this.myFormR.get('cpC').hasError('max')
    
    this.calleCEsVacio = this.myFormR.get('calleC').hasError('required')

    
    this.numeroCesVacio = this.myFormR.get('numeroC').hasError('required')

      
    this.numeroCesValido = !this.myFormR.get('numeroC').hasError('pattern')

 
      if((!this.correoCesVacio) &&
      (this.correoCesValido) &&
      (!this.nombreCesVacio) &&
      (!this.telefonoCesVacio) &&
      (this.telefonoCesValido)&&
      (!this.estadoCesVacio)&&
      (!this.ciudadCesVacio)&&
      (!this.coloniaCesVacio)&&
      (!this.cpCEsVacio)&&
      (this.cpCesValido)&&
      (!this.calleCEsVacio)&&
      (!this.numeroCesVacio)&&
      (this.numeroCesValido) ){


      this.dataC.correoC = this.myFormR.get('correoC').value
      this.dataC.nombreC = this.myFormR.get('nombreC').value
      this.dataC.telefonoC = this.myFormR.get('telefonoC').value
      this.dataC.estadoC = this.myFormR.get('estadoC').value
      this.dataC.ciudadC = this.myFormR.get('ciudadC').value
      this.dataC.coloniaC = this.myFormR.get('coloniaC').value
      this.dataC.cpC = this.myFormR.get('cpC').value
      this.dataC.calleC = this.myFormR.get('calleC').value
      this.dataC.numeroC = this.myFormR.get('numeroC').value

        
        
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
            this.correoCesValido =false;
            
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
        
      }
      
      /**
       * Función que sube los datos del vendedor al observable que es el servicio de registrar ademas de verificar
       * que los datos son correctos
       */
      
      submitV() {
        this.enviadoV = true;

      this.correoVesVacio = this.myFormR.get('correoV').hasError('required')
      this.correoVesValido = !this.myFormR.get('correoV').hasError('email')
      
      this.nombreVesVacio = this.myFormR.get('nombreV').hasError('required')
      
      
      this.telefonoVesVacio = this.myFormR.get('telefonoV').hasError('required')
      this.telefonoVesValido = !this.myFormR.get('telefonoV').hasError('pattern')

     

    this.estadoVesVacio = this.myFormR.get('estadoV').hasError('required') 
    
    this.ciudadVesVacio = this.myFormR.get('ciudadV').hasError('required') 

    
    this.coloniaVesVacio = this.myFormR.get('coloniaV').hasError('required')
    
    this.cpVEsVacio = this.myFormR.get('cpV').hasError('required')
 
    
    this.cpVesValido = !this.myFormR.get('cpV').hasError('min') && !this.myFormR.get('cpV').hasError('max')
    
    this.calleVEsVacio = this.myFormR.get('calleV').hasError('required')

    
    this.numeroVesVacio = this.myFormR.get('numeroV').hasError('required')

      
    this.numeroVesValido = !this.myFormR.get('numeroV').hasError('pattern')

    this.tarjetaEsVacia = this.myFormR.get('tarjeta').hasError('required')

    
    this.tarjetaEsValida = !this.myFormR.get('tarjeta').hasError('pattern')
    
    


 
      if((!this.correoVesVacio) &&
      (this.correoVesValido) &&
      (!this.nombreVesVacio) &&
      (!this.telefonoVesVacio) &&
      (this.telefonoVesValido)&&
      (!this.estadoVesVacio)&&
      (!this.ciudadVesVacio)&&
      (!this.coloniaVesVacio)&&
      (!this.cpVEsVacio)&&
      (this.cpVesValido)&&
      (!this.calleVEsVacio)&&
      (!this.numeroVesVacio)&&
      (this.numeroVesValido&&
      (!this.tarjetaEsVacia)&&
      (this.tarjetaEsValida))){


      this.dataV.correoV = this.myFormR.get('correoV').value
      this.dataV.nombreV = this.myFormR.get('nombreV').value
      this.dataV.telefonoV = this.myFormR.get('telefonoV').value
      this.dataV.estadoV = this.myFormR.get('estadoV').value
      this.dataV.ciudadV = this.myFormR.get('ciudadV').value
      this.dataV.coloniaV = this.myFormR.get('coloniaV').value
      this.dataV.cpV = this.myFormR.get('cpV').value
      this.dataV.calleV = this.myFormR.get('calleV').value
      this.dataV.numeroV = this.myFormR.get('numeroV').value
      this.dataV.tarjetaV = this.myFormR.get('tarjeta').value


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
        this.correoVesValido = false;
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
}