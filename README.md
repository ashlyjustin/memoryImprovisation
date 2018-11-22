# memoryImprovisation

A QuerySet typically caches its results internally so that repeated evaluations do not result in additional queries. In contrast, iterator() will read results directly, without doing any caching at the QuerySet level

Two methods of retrieving data are provided in books/views.py and their memory usage is shown in their json output.
