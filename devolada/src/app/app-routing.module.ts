import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { InicioComponent } from './inicio/inicio.component';
import { ProductoComponent } from './producto/producto.component';
import { CarritoComponent } from './carrito/carrito.component';
import { DireccionComponent } from './direccion/direccion.component';
import { MetodoPagoComponent } from './metodo-pago/metodo-pago.component';
import { MisProductosComponent } from './mis-productos/mis-productos.component';
<<<<<<< HEAD
import { CompraFinalizadaComponent } from './compra-finalizada/compra-finalizada.component';
=======
import { CrearResenaComponent } from './crear-resena/crear-resena.component';
>>>>>>> 86f12f7312af2fa3c1885fd7f828c7b32532aae2

const routes: Routes = [
  {path: 'carrito', component: CarritoComponent},
  {path: 'metodo-pago', component: MetodoPagoComponent},
  {path: 'inicio', component: InicioComponent},
  {path: 'producto', component: ProductoComponent},
  {path: 'direccion', component: DireccionComponent},
  {path: 'mis-productos', component: MisProductosComponent},
<<<<<<< HEAD
  {path: 'compra-finalizada', component: CompraFinalizadaComponent}
=======
  {path: 'crear-resena', component: CrearResenaComponent},
>>>>>>> 86f12f7312af2fa3c1885fd7f828c7b32532aae2
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
