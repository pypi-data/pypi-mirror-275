from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='sharedkernel',
    author='Smilinno',
    packages=['sharedkernel','sharedkernel.database','sharedkernel.database.vector_database_repository','sharedkernel.enum','sharedkernel.exception','sharedkernel.objects'],
    # Needed for dependencies
    install_requires=['numpy','requests','pymongo','fastapi==0.89.1','PyJWT','pymilvus','chromadb'],
    # *strongly* suggested for sharing
    version='1.1.1',
    description='sharekernel is an shared package between all python projects',
)