	-- Must define the following, before any computations
	T = QQ[x,y,z]
	S = QQ[x,y]

	invars = f -> (
	<< "The function entered is: " << f << endl << endl,
	<< "Singular Locus: " << singularLocus(S/f) << endl << endl,
	partials = ideal(jacobian(f));
	sings = partials + ideal(f);
	tj = degree(sings);
	<< "Tjurina Number: " << tj << endl << endl,
	pd = primaryDecomposition(partials);
	<< "Here are the possible Milnor numbers: " << apply(pd, degree) << endl,
	milnor = degree(pd#0);
	<< "corresponding to the following ideals: " << apply(pd, radical) << endl << endl,
	idealList = primaryDecomposition(sings);
	<< "Singularities occur where the following ideals vanish: " << idealList << endl << endl,
	degArr = degree(f);
	deg = degArr#0;
	<< "Degree: " << deg << endl,
	arithGenus = binomial(deg - 1, 2);
	<< "Arithmetic Genus: " << arithGenus << endl,
	vanList = {};
	<< idealList << endl,
	for i from 1 to length(idealList) do (
		vanList = append(vanList, zeroDimSolve(idealList#(i-1)))
	),
	<< "Here are the locations of the singularities: " << vanList << endl,
	ptList = {};
	multList = {};
	for i from 1 to length(vanList) do (
		ptList = append(ptList, (coordinates vanList#(i-1)#0)#0),
		ptList = append(ptList, (coordinates vanList#(i-1)#0)#1),
		<< "[" << (coordinates vanList#(i-1)#0)#0 << ":" << (coordinates vanList#(i-1)#0)#1 << ":" << 1 << "]" << endl,
	),
	<< "Here is the point list: " << ptList << endl,
	use(T);
	f = substitute(f, T);
	fz = homogenize(f,z);
	for i from 0 to length(vanList) - 1 do (
		multList = append(multList, degree(tangentCone(ideal(substitute(fz, {x => x-promote(realPart(ptList#(i*2)), QQ), y => y-promote(realPart(ptList#(i*2 + 1)), QQ), z => z-promote(1, QQ)}))))),
	),
	<< "Multiplicities for Singularities: " << multList << endl,
	deltas = {};
	for i from 1 to length(multList) do (
		deltas = append(deltas, (0.5)*(multList#(i-1))*(multList#(i-1)-1))
	),
	<< "Delta invariants for each singularity: " << deltas << endl,
	delta = sum(deltas);
	<< "Total delta invariant: " << delta << endl,
	geoGenus = arithGenus - delta;
	<< "Geometric genus: " << geoGenus << endl,
	<< "Milnor Number: " << milnor << endl,
	branchings = {};
	for i from 1 to length(multList) do (
		branchings = append(branchings, 2*deltas#(i-1)+1-milnor),
	),
	<< "Branching numbers: " << branchings << endl,
	branching = 2*delta+1-milnor;
	<< "Total branching number: " << branching << endl,
	)
