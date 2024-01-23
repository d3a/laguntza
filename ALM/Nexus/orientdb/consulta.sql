connect plocal:../sonatype-work/nexus3/db/component admin admin;

select name, size    from asset    where format != 'docker'      and size > 123456    order by size desc    limit 10000;

exit
