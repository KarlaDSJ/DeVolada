import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { InicioComponent } from './inicio/inicio.component';
import { ProductoComponent } from './producto/producto.component';
import { CarritoComponent } from './carrito/carrito.component';
import { DireccionComponent } from './direccion/direccion.component';
import { MetodoPagoComponent } from './metodo-pago/metodo-pago.component';
import { MisProductosComponent } from './mis-productos/mis-productos.component';
import { CrearResenaComponent } from './crear-resena/crear-resena.component';

const routes: Routes = [
  {path: 'carrito', component: CarritoComponent},
  {path: 'metodo-pago', component: MetodoPagoComponent},
  {path: 'inicio', component: InicioComponent},
  {path: 'producto', component: ProductoComponent},
  {path: 'direccion', component: DireccionComponent},
  {path: 'mis-productos', component: MisProductosComponent},
  {path: 'crear-resena', component: CrearResenaComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
