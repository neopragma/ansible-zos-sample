//IBMUSER1 JOB ,'ADMIN',
//            CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),
//            NOTIFY=&SYSUID
//********************************************************************
//* SAMPLE JOB THAT ALLOCATES A SOURCE LIBRARY FOR A SOFTWARE ENGINEER
//********************************************************************
//CLEANUP  EXEC PGM=IEFBR14
//OLDLIB   DD DSN=PLAT01.DEV.JCL,
//            DISP=(MOD,DELETE,DELETE),
//            UNIT=SYSDA,VOL=SER=USRVS1,
//            SPACE=(TRK,(0)),
//            DCB=(DSORG=PO,RECFM=FB,LRECL=80,BLKSIZE=0),
//            DSNTYPE=LIBRARY
//ALLOC    EXEC PGM=IEFBR14
//NEWLIB   DD DSN=PLAT01.DEV.JCL,
//            DISP=(NEW,CATLG,DELETE),
//            UNIT=SYSDA,VOL=SER=USRVS1,
//            SPACE=(TRK,(2,4),RLSE),
//            DCB=(DSORG=PO,RECFM=FB,LRECL=80,BLKSIZE=0),
//            DSNTYPE=LIBRARY
