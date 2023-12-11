Info<< "Reading transportProperties\n" << endl;

IOdictionary transportProperties
(
    IOobject
    (
        "transportProperties",
        runTime.constant(),
        mesh,
        IOobject::MUST_READ_IF_MODIFIED,
        IOobject::NO_WRITE
    )
);
///////////////////////////////////////// vlaues which is needed for new equations////////////////

dimensionedScalar Cmu
    (
       transportProperties.lookup("Cmu")
    );
dimensionedScalar C1
    (
       transportProperties.lookup("c1")
    );
dimensionedScalar C2
    (
       transportProperties.lookup("c2")
    );
dimensionedScalar sigmaEps
    (
       transportProperties.lookup("sigmaEps")
    );
dimensionedScalar sigmaK
    (
       transportProperties.lookup("sigmaK")
    );

///////////////////////////////////// these values are defined because they are always >0 //////////////////
    dimensionedScalar kmin  
    (
       "kmin", dimensionSet(0, 2, -2, 0, 0), 0
    );
    dimensionedScalar epsmin
    (
       "epsmin", dimensionSet(0, 2, -3, 0, 0), 0
    );
    dimensionedScalar numin
    (
       "numin", dimensionSet(0, 2, -1, 0, 0), 0
    );

Info<< "Reading field epsilon (passive scalar 1)\n" << endl;
volScalarField epsilon
(
    IOobject
    (
        "epsilon",
        runTime.timeName(),
        mesh,
        IOobject::MUST_READ,
        IOobject::AUTO_WRITE
    ),
    mesh
);

Info<< "Reading field k (passive scalar 1)\n" << endl;
volScalarField k
(
    IOobject
    (
        "k",
        runTime.timeName(),
        mesh,
        IOobject::MUST_READ,
        IOobject::AUTO_WRITE
    ),
    mesh
);

Info<< "Reading field nu_turbulence (passive scalar 1)\n" << endl;
volScalarField nu_turbulence
(
    IOobject
    (
        "nu_turbulence",
        runTime.timeName(),
        mesh,
        IOobject::MUST_READ,
        IOobject::AUTO_WRITE
    ),
    mesh
);

////////////////////////////////////////////////////////////////////////////////////////////////////



dimensionedScalar nu
(
    "nu",
    dimViscosity,
    transportProperties.lookup("nu")
);

Info<< "Reading field p\n" << endl;
volScalarField p
(
    IOobject
    (
        "p",
        runTime.timeName(),
        mesh,
        IOobject::MUST_READ,
        IOobject::AUTO_WRITE
    ),
    mesh
);


Info<< "Reading field U\n" << endl;
volVectorField U
(
    IOobject
    (
        "U",
        runTime.timeName(),
        mesh,
        IOobject::MUST_READ,
        IOobject::AUTO_WRITE
    ),
    mesh
);

#include "createPhi.H"

label pRefCell = 0;
scalar pRefValue = 0.0;
setRefCell(p, mesh.solutionDict().subDict("PISO"), pRefCell, pRefValue);
mesh.setFluxRequired(p.name());
