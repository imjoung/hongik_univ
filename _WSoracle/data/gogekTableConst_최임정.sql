DROP table gogek

CREATE table gogek(
gobun number(3), 
goname varchar2(10), 
gotel varchar2(20),
gojumin varchar2(14), 
godam number(3),
CONSTRAINT gogek_gobun_pk PRIMARY KEY (gobun),
CONSTRAINT gogek_godam_fk FOREIGN KEY (godam) REFERENCES sawon(sabun)
);


select owner , constraint_name, table_name
from user_constraints;