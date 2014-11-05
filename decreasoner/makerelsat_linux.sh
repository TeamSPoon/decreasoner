#
# Copyright (c) 2005 IBM Corporation and others.
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Common Public License v1.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/cpl-v10.html
#
# Contributors: 
# IBM - Initial implementation
# Mark J. Nelson (2008-04-19) - Update for relsat 2.02
#
cd software/relsat-dist
tar -xvf relsat_2.02.tar

sed -e 's/CFLAGS= -DNDEBUG -O3 -DNO_GMP/CFLAGS = -static -DNDEBUG -O3/g' Makefile.linux >Makefile1
#sed -e 's/^LIBS =/LIBS = \/usr\/lib\/libgmp.a/g' Makefile1 >Makefile2
sed -e 's/^LIBS =/LIBS = \/usr\/lib\/x86_64-linux-gnu\/libgmp.a/g' Makefile1 >Makefile2
make -f Makefile2
mv relsat ../../solvers
