import { TestBed } from '@angular/core/testing';

import { DireccionGuard } from './direccion.guard';

describe('DireccionGuard', () => {
  let guard: DireccionGuard;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    guard = TestBed.inject(DireccionGuard);
  });

  it('should be created', () => {
    expect(guard).toBeTruthy();
  });
});
